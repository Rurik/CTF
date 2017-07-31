import base64
for i in open('a.txt').readlines():
    z = base64.b64decode(i)
    print z.encode('hex')