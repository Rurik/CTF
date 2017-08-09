import base64
import codecs
import hashlib
import string
import struct
import zlib


def a():
    print('start')
    for i in range(256):
        x, y = Level4_XOR(i)
        if x == 0x8601f50b: print(i)

def Level4_XOR(val):
    a = (0x100000001B3 * (val ^ 0xCBF29CE484222325))
    return a & 0xFFFFFFFF, (a & 0xFFFFFFFF00000000) >> 32

def Level4():
    print('Reading lvl4 hex')
    result = ''
    cnt = 0
    data = open('lvl4_hex.dat', 'rb')
    for a in range(0, 580, 8):
        print('=========')
        data.seek(a)
        check = data.read(4)
        check = struct.unpack('I', check)[0]
        check2 = data.read(4)
        check2 = struct.unpack('I', check2)[0]
        #print(a, check, check2)
        #print(codecs.encode(check, 'hex_codec'))
#    hexes = open('level4_hex.txt', 'r').readlines()
#    for check in hexes:
#        check = check.split()[-1].strip('h')
#        check = int(check, 16)
        for i in range(0xFF):
            chk, chkhi = Level4_XOR(i)
            if chk == check and chkhi == check2:
                result += chr(i)
                print(hex(check), chr(i), hex(cnt))
                cnt += 1
                #continue
    print(result)
    std_base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    my_base64chars  = "PANDEFGHIJKLMCOBQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    ENCODE_TRANS = string.maketrans(std_base64chars, my_base64chars)
    DECODE_TRANS = string.maketrans(my_base64chars, std_base64chars)
    print(base64.b64decode(result.translate(DECODE_TRANS)))
    """
    b = base64.b64decode(result)
    print(b)
    print(base64.b64encode(b))
    #alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/PANDAPANDAPANDAPANDAPANDAPabcdefghijklmnopqrstuvwxyz0123456789+/PANDEFGHIJKLMCOBQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/QpaZIivj4ndG=H021y+NO5RSa/xPgUz67FMhYq8b3wemKfkJLBocCDrs9VtWXlEu1OnZyI5vyCFn+Yf=NOV2Oii+ODy55qUTR5wncUj5rUsFVzhQB=h=CHNTs0ZYmGLAAabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/QpaZIivj4ndGH021y+NO5RST/xPgUz67FMhYq8b3wemKfkJLBocCDrs9VtWXlEuA"
    s = b.translate(string.maketrans(my_base64chars, std_base64chars))
    print(s)
    data = base64.b64decode(s+'==')
    z = 'UEFOREEgUEFOREEgUEFOREEhIEJAU0U2CNAQQU5EQSAGTlY2CNAQQU5EQSAYT1IgUEFOREE='
    z = z.translate(string.maketrans(my_base64chars, std_base64chars))
    print(base64.b64decode(z))
    """




def main():
    Level4()

if __name__ == '__main__':
    main()
