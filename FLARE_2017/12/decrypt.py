import base64
import hashlib
import io
import os
import socket
import struct
import sys
import zipfile
import zlib
from collections import Counter

import aplib
import dpkt
import lzo
import xtea
from Crypto.Cipher import AES, ARC4, DES3, Blowfish
from Crypto.Util.Padding import unpad
from cryptography.hazmat.decrepit.ciphers.algorithms import Camellia
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from elftools.elf.elffile import ELFFile

PCAP = '20170801_1300_filtered.pcap'

# Pulled this from:
#     c:\staging\cf.exe lab10.zip tCqlc2+fFiLcuq1ee1eAPOMjxcdijh8z0jrakMA/jxg=
AES_KEY = base64.b64decode('tCqlc2+fFiLcuq1ee1eAPOMjxcdijh8z0jrakMA/jxg=')

# From screenshot BMP
ZIP_PASS = b'infectedinfectedinfectedinfectedinfected919'

# The CMD_FILE transfer carrying lab10.zip.cry
ZIP_SESSION = bytes.fromhex('9a53bd7d77d0e62867dd3d7c9d737cac')

FLAG_ADDR, FLAG_LEN = 0x4b0fa0, 0x31


# --- plugin signatures -----------------------------------------------------
MAGIC_RC4      = bytes.fromhex('c30b1a2dcb489ca8a724376469cf6782')
MAGIC_TRANSP   = bytes.fromhex('38be0f624ce274fc61f75c90cb3f5915')
MAGIC_BASE64   = bytes.fromhex('ba0504fcc08f9121d16fd3fed1710e60')
MAGIC_XTEA     = bytes.fromhex('b2e5490d2654059bbbab7f2a67fe5ff4')
MAGIC_BLOWFISH = bytes.fromhex('2965e4a19b6e9d9473f5f54dfef93533')
MAGIC_3DES     = bytes.fromhex('46c5525904f473ace7bb8cb58b29968a')
MAGIC_CAMELLIA = bytes.fromhex('9b1f6ec7d9b42bf7758a094a2186986b')
MAGIC_XOR      = bytes.fromhex('8746e7b7b0c1b9cf3f11ecae78a3a4bc')
MAGIC_ZLIB     = bytes.fromhex('5fd8ea0e9d0a92cbe425109690ce7da2')
MAGIC_APLIB    = bytes.fromhex('503b6412c75a7c7558d1c92683225449')
MAGIC_LZO      = bytes.fromhex('0a7874d2478a7713705e13dd9b31a6b1')

# Command types: no crypto, the payload passes straight through.
MAGIC_FILE   = bytes.fromhex('f47c51070fa8698064b65b3b6e7d30c6')
MAGIC_SHELL  = bytes.fromhex('f46d09704b40275fb33790a362762e56')
MAGIC_XFER   = bytes.fromhex('a3aecca1cb4faa7a9a594d138a1bfbd5')
MAGIC_TUNNEL = bytes.fromhex('77d6ce92347337aeb14510807ee9d7be')
MAGIC_MAIN1  = bytes.fromhex('f37126ad88a5617eaf06000d424c5a21')
MAGIC_MAIN2  = bytes.fromhex('155bbf4a1efe1517734604b9d42b80e8')
MAGIC_MAIN3  = bytes.fromhex('51298f741667d7ed2941950106f50545')

MAGIC_NAMES = {
    MAGIC_RC4: 'RC4', MAGIC_TRANSP: 'TRANSP', MAGIC_BASE64: 'BASE64',
    MAGIC_XTEA: 'XTEA', MAGIC_BLOWFISH: 'BLOWFISH', MAGIC_3DES: '3DES',
    MAGIC_CAMELLIA: 'CAMELLIA', MAGIC_XOR: 'XOR', MAGIC_ZLIB: 'ZLIB',
    MAGIC_APLIB: 'APLIB', MAGIC_LZO: 'LZO',
    MAGIC_FILE: 'CMD_FILE', MAGIC_SHELL: 'CMD_SHELL', MAGIC_XFER: 'CMD_XFER',
    MAGIC_TUNNEL: 'CMD_TUNNEL', MAGIC_MAIN1: 'MAIN1', MAGIC_MAIN2: 'MAIN2',
    MAGIC_MAIN3: 'MAIN3',
}

ALL_MAGICS = [
    MAGIC_RC4, MAGIC_TRANSP, MAGIC_BASE64, MAGIC_XTEA, MAGIC_BLOWFISH, MAGIC_3DES,
    MAGIC_CAMELLIA, MAGIC_XOR, MAGIC_ZLIB, MAGIC_APLIB, MAGIC_LZO,
    MAGIC_FILE, MAGIC_SHELL, MAGIC_XFER, MAGIC_TUNNEL,
    MAGIC_MAIN1, MAGIC_MAIN2, MAGIC_MAIN3,
]

# Bytes of required data for each plugin in header
KEY_SIZES = {
    MAGIC_RC4:      16,
    MAGIC_XTEA:     16 + 8,      # key + iv
    MAGIC_BLOWFISH: 16 + 8,
    MAGIC_3DES:     24 + 8,
    MAGIC_CAMELLIA: 16,
    MAGIC_XOR:      4,
}


# Substitution table for the TRANSP plugin: out = TRANSP_TABLE[in]
TRANSP_TABLE = bytes.fromhex(
    'c719300ca810add5d41652fc1b827d323401e64c12082bf7ac8b3f67487221dc'
    'edf685b84f5f530a0428dfd87e063d034036687325b75d1ed20dc6c322f2200e'
    '17cc605c51c21d4acb331cf866836b3e27e39ff53aaa8a267f5a42cf7c075871'
    'eb05ba294b7ae0ec9a7b2e37fea4be49de00c5bb96e9c4799987f4131a1563f9'
    'a0d102d6091fe5926ae71843916e41c8a3b22cee8da65bef24b975570f6f1147'
    '9b3b76e19d6454a7c155b38931fdabb194b6142ff3bc69bfa180590bbdc92ad7'
    '813c23d3f1faea39389e5eb54561ff4e774d659ce8d993af50a284887898e286'
    'cedd8c8ea99570aee4ca62cd90c0fbb0dbb4d097f02d46da6c6d4474a58f5635')

# Custom Base64 table (see, Base64 CAN be encryption...)
B64_TABLE = bytes.maketrans(
    b'B7wAOjbXLsD+S24/tcgHYqFRdVKTp0ixlGIMCf8zvE5eoN1uyU93Wm6rZPQaJhkn',
    b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')


def trim_to_block(data, block_size):
    return data
    extra = len(data) % block_size
    if extra:
        data = data[:len(data) - extra]
    return data


def decrypt_rc4(key, data):
    return ARC4.new(key).decrypt(data)


def decrypt_transp(data):
    return bytes(TRANSP_TABLE[b] for b in data)


def decrypt_base64(data):
    return base64.b64decode(data.translate(B64_TABLE))


def decrypt_xtea(key, iv, data):
    cipher = xtea.new(key, mode=xtea.MODE_CBC, IV=iv)
    return cipher.decrypt(data)


def decrypt_blowfish(key, iv, data):
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, IV=iv)
    return cipher.decrypt(trim_to_block(data, 8))


def decrypt_3des(key, iv, data):
    cipher = DES3.new(key, DES3.MODE_CBC, IV=iv)
    return cipher.decrypt(trim_to_block(data, 8))


def decrypt_camellia(key, data):
    cipher = Cipher(Camellia(key), modes.ECB()).decryptor()
    return cipher.update(trim_to_block(data, 16)) + cipher.finalize()


def decrypt_xor(key, data):
    """Each 4-byte word XORed with the same 4-byte key."""
    key_word = struct.unpack('<I', key)[0]
    out = bytearray()
    for offset in range(0, len(trim_to_block(data, 4)), 4):
        word = struct.unpack_from('<I', data, offset)[0]
        out += struct.pack('<I', word ^ key_word)
    return bytes(out)


def decompress_zlib(data):
    return zlib.decompress(data)


def decompress_aplib(data):
    if data[:4] == b'AP32':
        header_size, packed_size = struct.unpack_from('<II', data, 4)
        data = data[header_size:header_size + packed_size]
    return bytes(aplib.APLib(data, strict=False).depack())


def decompress_lzo(data, out_len):
    return lzo.decompress(data, False, out_len)


def run_plugin(magic, inf, data_len, out_len):
    # Comms broken into various malware C2 plugins
    # broke these out into seperate functions for easy troubleshooting
    if magic == MAGIC_RC4:
        key = inf.read(16)
        return decrypt_rc4(key, inf.read(data_len))

    if magic == MAGIC_TRANSP:
        return decrypt_transp(inf.read(data_len))

    if magic == MAGIC_BASE64:
        return decrypt_base64(inf.read(data_len))

    if magic == MAGIC_XTEA:
        key = inf.read(16)
        iv = inf.read(8)
        return decrypt_xtea(key, iv, inf.read(data_len))

    if magic == MAGIC_BLOWFISH:
        key = inf.read(16)
        iv = inf.read(8)
        return decrypt_blowfish(key, iv, inf.read(data_len))

    if magic == MAGIC_3DES:
        key = inf.read(24)
        iv = inf.read(8)
        return decrypt_3des(key, iv, inf.read(data_len))

    if magic == MAGIC_CAMELLIA:
        key = inf.read(16)
        return decrypt_camellia(key, inf.read(data_len))

    if magic == MAGIC_XOR:
        key = inf.read(4)
        return decrypt_xor(key, inf.read(data_len))

    if magic == MAGIC_ZLIB:
        return decompress_zlib(inf.read(data_len))

    if magic == MAGIC_APLIB:
        return decompress_aplib(inf.read(data_len))

    if magic == MAGIC_LZO:
        return decompress_lzo(inf.read(data_len), out_len)

    # If none, then just give data back
    return inf.read(data_len)


# --- frames ----------------------------------------------------------------
def decode_frame(inf, magic):
    """
    Outer layer of a frame is prefixed with '2017' and crc
    Inner layer same fields without it
    """
    if magic:
        inf.read(8)  # b'2017' and crc
    inf.read(4)      # header length
    data_len, out_len = struct.unpack('<II', inf.read(8))
    magic = inf.read(16)
    return run_plugin(magic, inf, data_len, out_len)


def decode_stream(stream, outer_seen=None, inner_seen=None):
    # Find every complete b'2017' frame in a stream and decode both layers

    payloads, pos = [], 0
    while True:
        at = stream.find(b'2017', pos)
        if at < 0 or at + 36 > len(stream):
            return payloads
        magic = stream[at + 20:at + 36]
        data_len = struct.unpack_from('<I', stream, at + 12)[0]
        size = 36 + KEY_SIZES.get(magic, 0) + data_len
        if magic not in ALL_MAGICS or at + size > len(stream):
            pos = at + 4                         # false hit, or truncated
            continue
        outer = decode_frame(io.BytesIO(stream[at:at + size]), True)
        payloads.append(decode_frame(io.BytesIO(outer), False))
        if outer_seen is not None:
            outer_seen[MAGIC_NAMES.get(magic, 'unknown')] += 1
        if inner_seen is not None:
            inner_seen[MAGIC_NAMES.get(outer[12:28], 'unknown')] += 1
        pos = at + size


def tcp_streams(path):
    # Reassemble each TCP flow from the capture
    flows = {}
    with open(path, 'rb') as fh:
        for _ts, buf in dpkt.pcap.Reader(fh):
            try:
                ip = dpkt.ethernet.Ethernet(buf).data
                tcp = ip.data
                if not tcp.data:
                    continue
            except Exception:
                continue
            key = (socket.inet_ntoa(ip.src), tcp.sport,
                   socket.inet_ntoa(ip.dst), tcp.dport)
            flows.setdefault(key, []).append((tcp.seq, bytes(tcp.data)))

    streams = []
    for parts in flows.values():
        buf, expect = bytearray(), None
        for seq, data in sorted(parts):
            if expect is not None and seq < expect:
                data = data[expect - seq:]    # retransmit
                seq = expect
            elif expect is not None and seq > expect:
                buf += b'\x00' * (seq - expect)  # missing from the capture
            buf += data
            expect = seq + len(data)
        streams.append(bytes(buf))
    return streams


# --- payloads --------------------------------------------------------------
def tunnelled(payloads):
    #CMD_TUNNEL, sub==3 payload
    return b''.join(p[0x24:] for p in payloads if struct.unpack_from('<I', p, 4)[0] == 3)


def shell_lines(payloads):
    # Each operator command from shell session
    seen = set()
    for payload in payloads:
        text = payload[36:].decode('ascii', 'replace')
        first = next((l for l in text.split('\n') if l.strip()), '').strip()
        if first and first not in seen:
            seen.add(first)
            yield first


def recreate_zip(payloads):
    # Recreate lab10.zip.cry from CMD_FILE chunks
    chunks = {}
    file_size = None
    chunk_size = None
    for payload in payloads:
        at = payload.find(MAGIC_FILE)
        if at < 0 or payload[at + 16:at + 32] != ZIP_SESSION:
            continue
        fields = payload[at + 32:]
        if len(fields) < 24:
            continue
        offset, _, total, _, length, _ = struct.unpack_from('<6I', fields, 0)
        if total and length and offset < total:
            file_size = total
            chunks[offset] = fields[24:24 + length]

    offsets = sorted(chunks)
    chunk_size = offsets[1] - offsets[0] if len(offsets) > 1 else file_size

    want = (file_size + chunk_size - 1) // chunk_size
    return b''.join(chunks[i * chunk_size] for i in range(want))[:file_size]



def decrypt_archive(blob):
    """
    cf.exe's container:  b'cryp' + IV(16) + SHA256(32) + AES-256-CBC
    and inside it:       path_len(4) + path + zip_size(8) + zip + PKCS7
    """
    iv, digest = blob[4:20], blob[20:52]
    plain = unpad(AES.new(AES_KEY, AES.MODE_CBC, iv).decrypt(blob[52:]), 16)

    path_len = struct.unpack_from('<I', plain, 0)[0]
    at = 4 + path_len
    size = struct.unpack_from('<Q', plain, at)[0]
    archive = plain[at + 8:at + 8 + size]
    return archive

def message_types(payloads):
    return Counter(MAGIC_NAMES.get(p[20:36], 'unknown')
                   for p in payloads if len(p) >= 36)


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pcap = sys.argv[1] if len(sys.argv) > 1 else PCAP

    print('C2 channel on the first victim')
    print('[*] reassembling tcp flows from %s' % pcap)
    streams = tcp_streams(pcap)
    print('    %d flows, %s bytes of stream data'
          % (len(streams), format(sum(len(s) for s in streams), ',')))
    print("[*] decoding '2017' frames:")
    outer, inner = Counter(), Counter()
    stage2 = [p for s in streams for p in decode_stream(s, outer, inner)]
    print('    %d frames decoded' % len(stage2))
    print('outer plugins: ', outer)
    print('inner plugins: ', inner)
    print('message types: ', message_types(stage2))

    print('[*] 2nd transmissions')
    tunnel = tunnelled(stage2)
    print('    %s bytes' % format(len(tunnel), ','))
    outer, inner = Counter(), Counter()
    stage3 = decode_stream(tunnel, outer, inner)
    print('    %d frames decoded' % len(stage3))
    print('message types: ', message_types(stage3))

    print("[*] shell session:\n\n")
    for line in shell_lines(stage3):
        if line.isascii(): #if 'cf.exe' in line or 'lab10' in line:
            print('    %s' % line)

    print('\n\n[*] CMD_FILE session %s'
          % (ZIP_SESSION[:4].hex()))
    blob = recreate_zip(stage3)
    archive = decrypt_archive(blob)
    with open('lab10.zip', 'wb') as fh:
        fh.write(archive)
    print('[+] wrote lab10.zip, %s bytes' % format(len(archive), ','))


if __name__ == '__main__':
    main()
