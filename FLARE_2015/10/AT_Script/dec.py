from Crypto.Cipher import ARC4 as cipher
dec = cipher.new("flarebearstare")
x = '96D587B8139933D17E3598505E729DA736BB66AA6CFA5180289FB6845530'.decode('hex') # _StartService("", "challenge")
x = '9aee96b50da818d16f368556131aecfc69ef21a440f24fcc6bd1f3bd1e76db69574a6c8d81ed53688a7eaa364e53fd0700'.decode('hex')
x = '96c581bc009905e76931875a583f97a738b764eb67f35c802194bf86123b943d1907619488a31a26cf29ba5f5e57ed5c5a37cb5d67dc2020a7e6d55cadefba32aba3ed77f0e18e41a571e74a8a7614a895d7c8827c46028761994543bf449138c65a6e7b5039792c85be5b4998c9950d2497f73cd88d186a6bffe3634bd250ec59e2'.decode('hex')
y = dec.decrypt(x)
#enc.decrypt(x)
print y