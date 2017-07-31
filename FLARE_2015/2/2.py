import sys
orig = '\xAF\xAA\xAD\xEB\xAE\xAA\xEC\xA4\xBA\xAF\xAE\xAA\x8A\xC0\xA7\xB0\xBC\x9A\xBA\xA5\xA5\xBA\xAF\xB8\x9D\xB8\xF9\xAE\x9D\xAB\xB4\xBC\xB6\xB3\x90\x9A\xA8'
orig = orig[::-1]

def rol(byte, count):
    byte = (byte << count | byte >> (8 - count)) & 0xFF
    return byte

d = False
#a_h111111111111111111111111111111111111111111111111
bx = dx = 0



pw =  sys.argv[1]
for i in range(0, len(pw)):
    if d: print("")
    dx = bx & 0x3
    a = ord(pw[i]) ^ 0x1C7
    al = a & 0xFF
    ah = (a & 0xFF00) >> 8
    if d: print("DX: ", hex(dx))
    if d: print("A : ", hex(a))
    if d: print("AL: ", hex(al))
    if d: print("AH: ", hex(ah))
    if d: print("AH:  0x%02X   ROL(%02X): %02X" % ((ah), (dx), (rol(ah, dx))))
    ah = rol(ah, dx)
    a2 = ah + al + 1 # +1 for ADC carry
    #if d: print hex(dx), hex(a), hex(al), hex(ah), hex(a2)
    #if d: print "pw[i]: %s\tbx: 0x%02x\ta2: 0x%x" % (pw[i], dx, a2)
    bx = bx + a2
    if d: print("EndRound: ", i, hex(a2), hex(ord(orig[i])), " BX now: ", hex(bx))
    if chr(a2) == orig[i]:
        print("FOUND!!! ", pw)
    if not chr(a2) == orig[i]:
        if d: print("NOT FOUND")
        quit()





"""
Method 3
for byte in range(0, len(orig)):
    found = False
    for z in range(97, 123):
        if found:
            break
        pw = new + chr(z)
        if d: print chr(z)
        if d: print "PW: %s" % pw
        for i in range(0, len(pw)):
            dx = (bx + 0xb3) & 0x3
            a = ord(pw[i]) ^ 0x1C7
            al = a & 0xFF
            ah = (a & 0xFF00) >> 8
            a2 = ah + al + 1 # +1 for ADC carry
            #if d: print "pw[i]: %s\tbx: 0x%02x\ta2: 0x%x" % (pw[i], bx, a2)
            bx = a2
            
            if d: print byte, hex(a2), hex(ord(orig[byte]))
            if chr(a2) == orig[byte]:
                new = new + pw[i]
                found = True
                break
            
        zpass += 1
"""










"""
Method `1
for i in range(0, len(pw)):
    dx = dx + 0xb3
    dx = dx & 0x3
    a = ord(pw[i]) ^ 0x1C7
    al = a & 0xFF
    ah = (a & 0xFF00) >> 8
    a2 = ah + al + 1 # +1 for ADC carry
    #if d: print hex(bx), hex(a), hex(al), hex(ah), hex(a2)
    if d: print "pw[i]: %s\tbx: 0x%02x\ta2: 0x%x" % (pw[i], bx, a2)
    bx = a2
    
    if not chr(a2) == orig[i]:
        quit()
"""
    
    

"""
pw = 'ayyvs6789012345@flare-on.com1234567'
pw = 'ab                                 '
result = ''
bx = dx = 0
pw = 'a'
for z in range(97, 123):
    if d: print "PW:", pw
    pw2 = pw + chr(z) + '_'* 25
    for i in range(0, len(pw)):
        dx = dx + 0xb3
        dx = dx & 0x3
        a = ord(pw[i]) ^ 0x1C7
        al = a & 0xFF
        ah = (a & 0xFF00) >> 8
        a2 = ah + al + 1 # +1 for ADC carry
        #if d: print i, pw[i]
        #if d: print hex(bx), hex(a), hex(al), hex(ah), hex(a2)
        #if d: print "pw[i]: %s\tbx: 0x%02x\ta2: 0x%x" % (pw[i], bx, a2)
        bx = a2
        if d: print chr(a2), orig[i]
        if chr(a2) == orig[i]:
            pw = pw + pw[i]
            if d: print pw
            break
"""