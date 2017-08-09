import base64
import codecs
import hashlib
import string
import struct
import zlib


def Lvl1_Text_Encoding(flag):
    table = dict()
    for pos in range(len(flag)):
        v2 = ord(flag[pos]) >> 1
        chk1 = ord(flag[pos]) ^ v2
        table[flag[pos]] = chr(chk1)
    return table

def Level1():
    lvl1key = '\x6D\x59\x30\x64\x4B\x57\x57\x6E\x30\x5B\x45\x4E\x5C\x58\x5A\x68\x64\x45\x3A\x30\x4E\x5C\x57\x30\x5A\x51\x53\x45\x7B\x67\x59\x4E\x5C\x30\x4C\x51\x4A\x30\x51\x59\x30\x57\x5A\x61\x53\x58\x4B\x61\x7E\x57\x30\x4A\x4E\x4B\x4F\x52\x4E\x4F\x4B\x57\x30\x56\x57\x4A\x5D\x54\x69\x67\x66\x30\x51\x59\x56\x30\x53\x4F\x5D\x5A\x7E\x30\x53\x45\x30\x4E\x5C\x57\x30\x6A\x67\x64\x67\x69\x66\x61\x7B\x75\x30\x51\x4B\x4E\x5D\x55\x5D\x52\x57\x4B\x30\x66\x51\x57\x56\x51\x5A\x4F\x4A\x30\x55\x58\x4B\x30\x6E\x5D\x69\x64\x30\x6B\x5D\x69\x68\x7A\x30\x58\x55\x30\x62\x4B\x67\x4E\x67\x30\x51\x4E\x30\x6E\x59\x58\x7A\x7A\x68\x4A\x39'
    lvl1key2 = '\x95\x8E\x59\x08\x39\x20\xE5\xE8\xB1\x32\xF7\x6D\xEE\x75\x36\xA3\xF6\xE9\x0A\xDE\xA4\x78\x01\x3E\x2E\xBA\xF8\x14\x61\x9C\x08\x95'
    x = 0
    flag = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-=+{}[]:";\'<>?,./\|`~ '
    table = Lvl1_Text_Encoding(flag)
    result = ''
    for i in lvl1key:
        for key, val in table.items():
            if i == val:
                result += key
    return result

def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1)+F(n-2)

def Level3():
    table = dict()
    fibs = open('3_fib.txt', 'r').readlines()
    for fib in fibs:
        items = fib.split()
        table[items[0]] = items[1]

    data = open('3_key.dat', 'rb').read()
    result = ''
    for i in range(0, len(data), 4):
        a = data[i:i+4]
        #print(i,i+4)
        val = struct.unpack('I', a)[0]
        #print(val, hex(val))
        for key, value in table.items():
            #print(val, key, value)
            if val == int(value):
                x = chr(int(key)+0x40)
                result += x
        #        print('Found! {}\t{}'.format(value, x))
            #print(values)
        #print(i*4)
    #test = 84 # T
    print(result)




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
    b = base64.b64decode(result)
    print(b, len(b))
    print(base64.b64encode(b))
    std_base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    my_base64chars  = "PANDAPANDAPANDAPANDAPANDAPabcdefghijklmnopqrstuvwxyz0123456789+/"
    my_base64chars  = "PANDEFHIHJKLMNOBQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    s = b.translate(bytes.maketrans(my_base64chars, std_base64chars))
    data = base64.b64decode(s)



def Level5():
    # scrap this
    url1 = "S+\xc2\xb0+\xff\xc3\xb7\xc3\xbap\xc2\xa6\xc2\xa1vGd\xc3\x91\xc2\xb0\xc3\xb1\xc2\xb7\xc2\xab\xc2\xb7+T+n\xc3\xbaG+T\xc3\xb3\xc2\xb0Gn\xc3\xba\xc3\x9fpT\xc2\xbfs\xc2\xa6\xc3\xba+T\xc2\xbfp\xc2\xbba\xc3\xa1T\xc3\xb1\xffp\xc3\x9f\xc2\xa1\xff+T+\xc3\xba\xc2\xb2\xc3\xb3\xc2\xabs\xc3\xb3"
    result = ''
    datax = open('pt5/2.bin', 'rb').read()
    key2 = 0x62  # b
    key3 = 0x79  # y
    data = list()
    print('start')
#    for i in range(len(data)):
#        data[i] == datax[i]
#        data[i] = data[i] ^ key2
    for i in range(256):
        #if (0x1000193 * (i ^ 0x811C9DC5)) & 0xFFFFFFFF == 0xE60C2C52: #c
        #if (0x1000193 * (i ^ 0x811C9DC5)) & 0xFFFFFFFF == 0xEA0C329E: #o
        #if (0x1000193 * (i ^ 0x811C9DC5)) & 0xFFFFFFFF == 0xE10C2473: #d
        if (0x1000193 * (i ^ 0x811C9DC5)) & 0xFFFFFFFF == 0xE00C22E0: #e
            print(chr(i))
    #second to last byte
    for i in range(256):
        crc32 = zlib.crc32(bytes([i])) ^ 0x4C11DB7
        print(i, hex(crc32))
        if (i ^ (i >> 1)) == 41:
            print(chr(i))
    #for i in range(len(url1)):
        #x = 0
        #if not (i & 1):
        #    x = (ord(url1[i]) ^ 0x40)
        #result += chr((x) ^ (ord(url1[i]) ^ 0xCC))
    return result



def main():
    #lvl1 = Level1()
    #print(lvl1)
    Level3()
    #Level4()
    #Level5()

if __name__ == '__main__':
    main()
