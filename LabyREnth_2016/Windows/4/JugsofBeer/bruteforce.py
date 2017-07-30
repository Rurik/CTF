import itertools

keylen = 32
max = 68

#key1 = (3,1,2)
#for i in range(3, keylen):
    #print i
"""
for key2 in itertools.product(range(1,4), repeat=29):
    guess = key1 + key2
    if sum(guess) == 68:
        print(guess)
        print(sum(guess))
        open('guesses.txt', 'a').write(str(guess)+'\n')
"""        

def validate(key):
    check = "0123456789"
    checkval = (0x00, 0x00, 0x0D, 0x07)
    checkval_total = (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x0D, 0x00, 0x00, 0x00,
                      0x00, 0x00, 0x00, 0x00, 0x30, 0x00, 0x31, 0x00, 0x32, 0x00, 0x33, 0x00, 0x34, 0x00, 0x35, 0x00, 
                      0x36, 0x00, 0x37, 0x00, 0x38, 0x00, 0x39, 0x00)


    keypos = sub_value = 0

    print key
    bytecheck1 = bytecheck2 = 0

    while keypos < len(key): #32
        bytecheck1 = bytecheck2 = 0

        print('-=-=-=-=-=-=-\nRound keypos: {}'.format(keypos))
        for i in range(0, 10):
            if check[i] != key[keypos]:
                bytecheck1 += 1
            else:
                break
        print('Check: {}\tKey: {}\tBytecheck1: {}'.format(check[i], key[keypos], bytecheck1))

        for i in range(0, 10):
            if check[i] != key[keypos + 1]:
                bytecheck2 += 1
            else:
                break
        print('Check: {}\tKey: {}\tBytecheck2: {}'.format(check[i], key[keypos], bytecheck2))

        if bytecheck1 != bytecheck2:
            if bytecheck2 == 1:
                sub_value = 19 #0x13
            elif bytecheck2 == 2:
                sub_value = 13 # 0x0D
            elif bytecheck2 == 3:
                sub_value = 7  # 0x07
        print('sub_value: {}'.format(sub_value))
    
        checkstart = 16 # round 2 #
        print('?? bytecheck1 * 4 + 4: {}'.format(checkval_total[bytecheck1 * 4 + 4]))
        val1 = checkval[bytecheck1]
        val1 += checkval[0]#bytecheck2
        print('Val1: {}'.format(val1))

        if val1 <= sub_value:
            #v9 = v11
            #v12 = 
            print('less')
            pass
        else:
            print('more')
            pass


        keypos += 2
        if keypos > 4:
            quit()
    

validate("31231231231231231231231231233233")

