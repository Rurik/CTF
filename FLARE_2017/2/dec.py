v4 = 0x04
flag = '\x0D\x26\x49\x45\x2A\x17\x78\x44\x2B\x6C\x5D\x5E\x45\x12\x2F\x17\x2B\x44\x6F\x6E\x56\x09\x5F\x45\x47\x73\x26\x0A\x0D\x13\x17\x48\x42\x01\x40\x4D\x0C\x02\x69'

v4 = 0x04
result = list()
for i in flag[::-1]:
    #print(i, (ord(i) ^ v4), chr(ord(i) ^ v4)),
    result.append(chr(ord(i) ^ v4))
    v4 = ord(i) ^ v4
print(''.join(result))
print(''.join(result[::-1]))