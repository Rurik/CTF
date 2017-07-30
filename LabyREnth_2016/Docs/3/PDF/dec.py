def multibyte_xor(data, key):
  from itertools import izip, cycle
  return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))

a = ")5512{nn666o8.454#$o\".,n6 5\")~7|%\x106u6x\x16&\x19\"\x10"
print(multibyte_xor(a, '\x41'))