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


ids = ['UDYs','1D7b','NmdE','1o3g','5ms1','V6Rr','YCVV','ODJF','1Dpx','KTxA','J9xu','ZW==']
fullid = 'UDYs1D7bNmdE1o3g5ms1V6RrYCVVODJF1DpxKTxAJ9xuZW=='.lower()

count = 0
FullRange = "!#$%()*+,-./0123456789=?@ABCDEFGHIJKLMNOPQRSTUVWXYZ^_`abcdefghijklmnopqrstuvwxyz{|}"
print FullRange
print ""
print fullid
a1 = "Sp1"
a2 = "cy_"
a3 = "7_l"
a4 = "aye"
a5 = "r_O"
a6 = "SI_"
a7 = "dip"
a8 = "@fl"

for test in itertools.product(FullRange, repeat=3):
    count += 1
    a = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + ''.join(test)
    z = base64.b64encode(enc(a)).lower()
    if not count % 100000: print count, z
    if z == fullid:
        print a.encode('hex')
    if z[0:36] == "udys1d7bnmde1o3g5ms1v6rrycvvodjf1dpx": 
        print ''.join(a)
