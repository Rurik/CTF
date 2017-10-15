import hashlib
import struct

data = open('./APK/assets/tspe', 'rb')
hdr = data.read(8)
size = struct.unpack('>i', data.read(4))[0]
arr = list()
for i in range(size / 3):
    arr.append('')

for i in range(size/3):
    val = struct.unpack('>h', data.read(2))[0]
    key = data.read(1)
    arr[val] = key

result =''.join(arr)
print(result)
print(hashlib.sha1(result).hexdigest())
"""
Give a man a fire and he'll be warm for a day. Set a man on fire and he'll be warm for the rest of his life.
5f1be3c9b081c40ddfc4a0238156008ee71e24a4
"""
