import base64
import itertools

pw = 'flarebearstareflarebearstareflarebearstareflarebearstareflarebearstareflarebearstareflarebearstareflarebearstareflarebearstareflarebearstare'


def enc(bytes):
    result = ''
    for i in range(0, len(bytes)):
        a = ord(bytes[i])
        b = ord(pw[i])
        try:
            result += chr( a + b & 0xFF)
        except TypeError:
            print "ERROR"
            print i, pw[i], bytes[i]
            print "DONE"
    return result

def dec(data):
    for i in range(0, len(data)):
        a = ord(data[i])
        b = ord(pw[i])
        c = a - b
        if c < 0: c = 256 + c
        print pw[i], a, b, c, chr(c)

FullRange = "!#$%()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}"

fullid = 'UDYs1D7bNmdE1o3g5ms1V6RrYCVVODJF1DpxKTxAJ9xuZW=='.lower()

ids = ['UDYs','1D7b','NmdE','1o3g','5ms1','V6Rr','YCVV','ODJF','1Dpx','KTxA','J9xu','ZW==']

#test = open('key.txt', 'r').readline()
test = "Sp1cy_7_layer_OSI_dip@flare-on.com"
print test
print enc(test)
print base64.b64encode(enc(test)).swapcase()
print 'UDYs1D7bNmdE1o3g5ms1V6RrYCVVODJF1DpxKTxAJ9xuZW=='
quit()



for i in range(0, 40):
    test = 'a' * i + 'flare-on.com'
    print base64.b64encode(enc(test))
quit()
print dec(base64.b64decode(fullid))
result = ''
for id in ids:
    for a in range(0, 256):
        for b in range(0, 256):
            for c in range(0, 256):
                attempt = chr(a) + chr(b) + chr(c)
                res = enc(attempt)
                fin = base64.b64encode(res)
                if fin == id:
                    print id, a, b, c, attempt, res
quit()

print enc('123')
print base64.b64encode(enc('123'))
quit()

data = base64.b64decode(ids[0])
print len(data)


"""
for i in range(0, len(data)):
    a = ord(data[i])
    b = ord(pw[i])
    c = a - b
    if c < 0: c = 128-c
    print pw[i], a, b, c, chr(c)
    
    result = chr(c)
print len(data)
"""
