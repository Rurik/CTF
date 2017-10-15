import pydasm

def disasm(fn, data):
    h = open(fn, 'w')
    offset = 0
    while offset < len(data):
        i = pydasm.get_instruction(data[offset:], pydasm.MODE_32)
        a = pydasm.get_instruction_string(i, pydasm.FORMAT_INTEL, 0)
        if a:
            h.write(a)
            h.write('\n')
        if not i:
            break
        offset += i.length
    h.close()

def x(data, key):
    result = ''
    for i in range(len(data)):
        result += chr(((ord(data[i]) ^ key) + 34 ) & 0xFF)
    return result


data = open('greek_to_me_orig.sc', 'rb').read()
for i in range(256):
    a = x(data, i)
    print('======= {} ======='.format(i))
    disasm('asm_{}.asm'.format(i), a)
    open('code.{}'.format(i), 'wb').write(a)
