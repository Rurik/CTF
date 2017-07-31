data = open('stack_buffer.txt', 'r').readlines()
z = ''
for i in data:
    a = i.split()[1]
    if not a == '0':
        z += chr(int(a))
print z


"""
md5 of that block in unicode = 
a = (189,26,226,231,215,1,30,181,228,8,115,172,98,174,39,189)
== bd1ae2e7d7011eb5e40873ac62ae27bd
BD1AE2E7D7011EB5E40873AC62AE27BD
"""