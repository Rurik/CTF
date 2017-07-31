def rol(byte, count):
    byte = (byte << count | byte >> (8 - count)) & 0xFF
    return byte

email = '\xAF\xAA\xAD\xEB\xAE\xAA\xEC\xA4\xBA\xAF\xAE\xAA\x8A\xC0\xA7\xB0\xBC\x9A\xBA\xA5\xA5\xBA\xAF\xB8\x9D\xB8\xF9\xAE\x9D\xAB\xB4\xBC\xB6\xB3\x90\x9A\xA8'
email = email[::-1]
AH = AL = AX = BX = DX = 0
result = ''

for i in range(0, len(email)):
    AH = rol(1, DX)
    AL = (ord(email[i]) - AH - 1) ^ 0xC7
    BX = BX + ord(email[i])
    DX = BX & 3
    result += chr(AL)
print(result)