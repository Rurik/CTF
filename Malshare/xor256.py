import sys

def xor256_inc(data, key):
# This does a 256-byte incrementing XOR, starting at character "Key"    
    def build_key(start):
        xor_key = ""
        for i in range(ord(start), 256):
            xor_key += chr(i)
        for i in range(0, ord(start)):
            xor_key += chr(i)
        return xor_key
    
    xor_key = build_key(key)
    result = ""
    for i in range(0, len(data)):
        x = i % 256
        result += chr(ord(data[i]) ^ ord(xor_key[x]))
    return result

def xor256_dec(data, key):
# This does a 256-byte decrementing XOR, starting at character "Key"    
    def build_key(start):
        xor_key = ""
        for i in range(ord(start), -1, -1):
            xor_key += chr(i)
        for i in range(255, ord(start), -1):
            xor_key += chr(i)
        return xor_key
    
    xor_key = build_key(key)
    result = ""
    for i in range(0, len(data)):
        x = i % 256
        result += chr(ord(data[i]) ^ ord(xor_key[x]))
    return result

def byte_swap_all(data):
    newstr = ""
    print len(data)
    for i in range(0, len(data), 2):
        try:
            newstr += data[i+1] + data[i]
        except:
            newstr += data[i]
    return newstr
	
try:
    fname = sys.argv[1]
    if sys.argv[2] == "+":
        inc = True
        dir = "Incrementing"
    elif sys.argv[2] == "-":
        inc = False
        dir = "Decrementing"
    xor = chr(int(sys.argv[3],16))
except:
    print "XOR 256. Version 1.2 - bbaskin"
    print "Usage: xor_256.py <file> [+|-] <hex key>"
    print "Input : Raw Data File, + or - sign, hex value"
    print "Example: xor256.py payload + 5F"
    print "Output: Data file with each byte XOR'd by 256-byte key, starting with <hex key>"
    quit()	
    
data = open(fname, "rb").read()
print  "%d bytes read" % len(data)
print "Using XOR key: %x, %s" % (ord(xor), dir)

if inc:
    unencrypted = xor256_inc(data, xor)
else:
    unencrypted = xor256_dec(data, xor)
open(fname+".dec", "wb").write(unencrypted)
#z = byte_swap_all(unencrypted)
#open(fname+".dec.swap", "wb").write(z)
