def multibyte_xor(data, key):
  from itertools import izip, cycle
  return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))

data = open('file.final.dat', 'rb').read()
result = multibyte_xor(data, '\xAA')
open('file.final.xor.dat', 'wb').write(result)
