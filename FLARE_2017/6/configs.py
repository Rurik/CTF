import numpy
data = open('configs.dat', 'rb')

seed = 0x18 + 0x52414E44
print(hex(seed))
numpy.random.seed(seed)
for i in range(0x18):
    decrypted = ''
    data.seek(i * 64)
    conf = data.read(64)
    x = numpy.random.rand()#int(0,90000)
    print(x)
    print(hex(x))
    quit()
    #for i in range(64):
        #decrypted += chr( ord(conf[i] ^ random.random
data.close()
#0x4Cf8 (19704) & 0xFF = 0xF8
#0x4d47 (19783) & 0xFF = 0x47
