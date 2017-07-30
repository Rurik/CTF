def RC4_KSA(key):
    S = range(256)
    j = 0
    out = []
    for i in range(256):
        j = (j + S[i] + ord( key[i % len(key)] )) % 256
        S[i] , S[j] = S[j] , S[i]
    return S

def RC4_PRGA(S, data):
    i = j = 0
    out = []
    for char in data:
        i = ( i + 1 ) % 256
        j = ( j + S[i] ) % 256
        S[i] , S[j] = S[j] , S[i]
        out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))
    return out

code = '\xBA\xAF\x4D\x55\x3C\xE3\x03\x22\xB0\xDF\xF3\xD3\x57\xD0\xE1\x40\xF9\x13\x1F\xBA\x8D\x12\xF1\xFF\x48\xC2\x8E\x00\xFD\x54\x97\x9D\x75\x71\x30\x8F\x43\x28\xFE\x69\x36\x47\x8F\xA2\xEF\x49\x74\x7C\xE1\x4C\x6F\x4F\xD4\x82'
count = 0
keyspace = 142848000
for c5 in range(12 + 0x2D, 1 + 0x2D, -1): # Month + 0x2D
    for c6 in range(11 + 0x5E, 32 + 0x5E): # Day + 0x5E
        print('Current date: {}/{}'.format(c6-0x5E, c5 - 0x2D))
        for c7 in range(0 + 0x4B, 25 + 0x4B): # Hour + 0x4B
            #for c8 in range(5 + 0x3C, 10 + 0x3C): # dwMajorVersion + 0x3C
            for c8 in range(5 + 0x3C, 11 + 0x3C): # dwMajorVersion + 0x3C
                for c9 in range(0 + 0x3F, 5 + 0x3F): # dwMajorVersion + 0x3F
                    for c10 in range(0x69, 0x6B): #FS30 0/1 + 0x69
                        for c11 in range(0, 256): #User Lang + 0x5E, could loop around
                            count += 1
                            key = 'b00!' + chr(c5) + chr(c6) + chr(c7) + chr(c8) + chr(c9) + chr(c10) + chr(c11)
                            sbox = RC4_KSA(key)
                            result = RC4_PRGA(sbox, code)
                            if not count % 100000: print('{}\t{}'.format(key, (count/keyspace)*100))
                            if result[0] == ('P') and result[1] == ('A') and result[2] == 'N' and result[3] == '{':
                                print(key)
                                print(key.encode('hex'))
                                print(result)
                                a = open('a.txt', 'a')
                                a.write(key + '\n')
                                a.write(key.encode('hex') + '\n')
                                a.write(result[0] + result[1] + result[2] + result[3] + result[4])
                                a.write('\n')
                                a.close()