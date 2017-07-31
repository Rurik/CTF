data = open('..\libvalidate.so')
offset = 0x4060
size = 6952
count = 23
data.seek(offset)
    
for i in range(count,0,-1):
    print i, offset, size, offset+size
    t = data.read(size)
    fn = str(i) + '.dat'
    open(fn, 'wb').write(t)
    
Should_hav
e_
g0
ne
_t
o_
ta
sh
13: i_
14: $t
at
io
n@flare-on.com

Should_have_g0ne_to_tash
13: i_
14: $tation@flare-on.com

Should_have_g0ne_to_tashi_$tation@flare-on.com
