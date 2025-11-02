import struct
import sys


def decrypt_str(data, seed):
    result = []
    i = 0

    while i < len(data) - 1:
        xor_key = ((seed * 0x19660d + 0x3c6ef35f) >> 24) & 0xFF
        result.append(data[i] ^ xor_key)

        seed = (seed * 0x17385ca9 + 0x47502932) & 0xFFFFFFFF

        xor_key = (seed >> 24) & 0xFF
        result.append(data[i + 1] ^ xor_key)

        i += 2

    if i < len(data):
        xor_key = ((seed * 0x19660d + 0x3c6ef35f) >> 24) & 0xFF
        result.append(data[i] ^ xor_key)
    return bytes(result)

with open('Huntress_HNTS.bin', 'rb') as f:
    data = f.read()

magic = data[:4].decode('utf-8')
count = struct.unpack('<I', data[4:8])[0]
print(f'Magic: {magic}')
print(f'Entries: {count}\n')

entries = []
offset = 8
for i in range(count):
    entry_id, data_offset, seed, data_size = struct.unpack('<IIII', data[offset:offset+16])
    encrypted = data[data_offset:data_offset+data_size]
    entries.append((entry_id, seed, encrypted))
    offset += 16

print('Parsing TOC')
for i, (entry_id, seed, encrypted) in enumerate(entries):
    print(f'[{i}] ID: 0x{entry_id:08x}, Seed: 0x{seed:08x}, Size: {len(encrypted)} bytes')

print('Strings:')
for i, (entry_id, seed, encrypted) in enumerate(entries):
    print(f'\n[{i}] ID: 0x{entry_id:08x}, Seed: 0x{seed:08x}, Raw size: {len(encrypted)}')
    
    decrypted = decrypt_str(encrypted, seed)
    print(f'    Encrypted: {encrypted.hex()}')
    print(f'    Decrypted: {decrypted.hex()}')

    text = decrypted.decode('utf-8', errors='ignore')
    print(f'    Text: {text}')
