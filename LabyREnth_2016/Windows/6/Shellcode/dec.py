def build_sbox(key):
    sbox = list()
    for i in range(0, 256): sbox.append(i)
    print(key)
    v9 = 0
    for i in range(0, 256):
        sbox_tmp = sbox[i]
        print('carryover bl: {}, key {}'.format(hex(v9), hex(ord(key[i % len(key)]))))
        v9 += (ord(key[i % len(key)]))
        v9 = v9 & 0xFF

        print 'Loop: {}, key: {}, current bl: {}'.format(i, key[i % len(key)], hex(v9))
        print 'Sum1: {} - {}'.format(v9, hex(v9))
        
        v9 = (sbox_tmp + v9) & 0xFF

        print 'Sum2: {} - {}'.format(v9, hex(v9))

        v11 = sbox[v9]
        sbox[i] = v11
        sbox[v11] = sbox_tmp
        

        for j in sbox: print(hex(j)),
        print '-=-=-='*10

    print
    #print(sbox)
    for i in sbox: print(hex(i)),


key = 'b00!4uCB@jb'
build_sbox(key)