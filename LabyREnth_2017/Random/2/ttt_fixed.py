import base64
iIi1IIIi1 = ''
O0oOoOOOoOO = 'XO'
for ii1ii11IIIiiI in range ( len ( o0OO0oOO0O0 ) ) :
    O00OOOoOoo0O = ii1ii11IIIiiI % 2
    iIi1IIIi1 += chr ( ord ( o0OO0oOO0O0 [ ii1ii11IIIiiI ] ) ^ ord ( O0oOoOOOoOO [ O00OOOoOoo0O ] ) )
#if 77 - 77: O0oo0OO0 % O0oo0OO0 * iiiiIi11i - i11iIiiIii
open('flag.png', 'wb').write(base64.b64decode(iIi1IIIi1))