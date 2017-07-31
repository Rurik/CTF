import base64, sys
import Crypto.Cipher.AES

buffer = (0xec, 0x35, 0xdd, 0x8f, 0xb3, 0xd9, 0xcb, 0x17, 0x57, 0x7e, 40, 0x41, 0x42, 230, 0x98, 180)
buffer2 = ( 0x1f, 100, 0x74, 0x61, 0, 0x54, 0x45, 0x15, 0x73, 0x61, 0x6d, 0x1d, 0x4f, 0x44, 0x15, 0x68, 
                0x73, 0x68, 0x15, 0x54, 0x4e)

z = ''
for i in z:
    z += i
    
z = ''
for i in range(0, len(buffer2)):
    z += chr( (buffer2[i]) ^ buffer[i % len(buffer)])
    
print z
"""    
password = base64.b64decode('PSCIQGfoZidjEuWtJAdn1JGYzKDonk9YblI0uv96O8s=') # See rgbKey
salt = base64.b64decode('ehjtnMiGhNhoxRuUzfBOXw==') # See rgbIV
aes = Crypto.Cipher.AES.new(password, Crypto.Cipher.AES.MODE_CBC, salt)
text = base64.b64decode('QpHn/fnraLswwI2Znt1xTaBzRtDqO4V5QI78jLOlVsbvaIs0yXMUlqJhQtK+su2hYn28G2vNyLkj0zLOs+RIjElCSqJv1aK/Yu8uY07oAeStqRt4u/DVUzoWlxdrlF0u')

print aes.decrypt(text)
"""