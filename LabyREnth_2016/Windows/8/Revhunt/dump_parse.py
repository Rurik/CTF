def revdword(str):
    result = ''
    for i in range(len(str)-2, -1, -2):
        result += str[i:i+2]
    return result

def decode(str):
    result = ''
    for i in range(0, len(str)):
        if not i % 2:
            result += chr( ord(str[i]) ^ 0x37)
        else:
            result += chr( ord(str[i]) ^ 0x13)
    return result

data = open('dump.txt', 'r').readlines()

#for i in range(len(data)-1, -1, -1):
result = ''
for i in range(0, len(data)):
    hexbytes = data[i].split()[-1].strip('h')
    result += (decode(hexbytes.decode('hex')))[::-1]
    #print(decode(hexbytes[::-1]))
    #print(decode((hexbytes).decode('hex')))
print(result)