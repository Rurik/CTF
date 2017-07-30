from Crypto.Cipher import AES as tiywynstbg
import base64 as ufjliotyds
import itertools as abtwsjxzys
from itertools import cycle, izip
def gasfewfesafds(message, key):
	return ''.join(chr(ord(c)^ord(k)) for c,k in abtwsjxzys.izip(message, abtwsjxzys.cycle(key)))

f5n0xha0d6v7knov = lambda c, e, f: c.decrypt(gasfewfesafds(ufjliotyds.b64decode(e), f))
oedceprc = tiywynstbg.new("ylbup1uuxvuhjtdau9q5logaeoojqvdq")
h9zsf6=f5n0xha0d6v7knov(oedceprc, "q/1wauNtJkVjvCW6zwvfb0a75wYjsBplvUBmw4H0Q15hYhyUJ2xN1izQnLw+wTfcKzlrXh7Qq7ibTBCLqlZEhhhCsi0tuDSBgD9i8Tmyq4pf8jPqGr6olubQ2qaPOsQGom7NikUVkZn4GP8SC4mGtjKcSpzS62jjHu1FhEK6ZqA=", "q2gws5fs")
print(h9zsf6)
		             
