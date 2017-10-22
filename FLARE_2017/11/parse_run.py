import sys
"""00000D80        .text:sub_401070+21             mov     ecx, [eax+edx*4+8]; arg2        ECX=00000467
00000D80        .text:sub_401070+2C             mov     ecx, [eax+edx*4+4]; arg1        ECX=00000000
00000D80        .text:sub_401070+37             mov     ecx, [eax+edx*4]; arg0
00000D80        .text:sub_401070+3F             call    sub_401000                      ESP=0018FF54
00000D80        .text:sub_401070+21             mov     ecx, [eax+edx*4+8]; arg2        ECX=00000000
00000D80        .text:sub_401070+2C             mov     ecx, [eax+edx*4+4]; arg1        ECX=00000466
00000D80        .text:sub_401070+37             mov     ecx, [eax+edx*4]; arg0
00000D80        .text:sub_401070+3F             call    sub_401000                      ESP=0018FF54
"""
block = open('covfefe_instructions.dat', 'rb').read()
data = open(sys.argv[1], 'r')
arg0 = arg1 = arg2 = arg0_d = arg1_d = arg2_d = current = reg = ''
while True:
    line = data.readline()
    if not line:
        quit()
    if 'arg0' in line:
        try:
            arg0 = int(line.split('ECX=0000')[1].strip(), 16)
        except IndexError:
            arg0 = int('0000', 16)
        arg0_d = block[arg0*4:arg0*4+4].encode('hex')
    elif 'arg1' in line:
        try:
            arg1 = int(line.split('ECX=0000')[1].strip(), 16)
        except IndexError:
            arg1 = int('0000', 16)
        arg1_d = block[arg1*4:arg1*4+4].encode('hex')
    elif 'arg2' in line:
        try:
            arg2 = int(line.split('ECX=0000')[1].strip(), 16)
        except IndexError:
            arg2 = int('0000', 16)
        arg2_d = block[arg2*4:arg2*4+4].encode('hex')
    elif '; pos' in line:
        current = line.split('ECX=0000')[1].strip()
    elif "[esi+edx*4]" in line:
        try:
            reg = line.split('EAX=')[1].split(' ')[0]
        except IndexError:
            reg = ''
        try:
            print('0x{}\tsub_401000({:04x}, {:04x}, {:04x})\t[{} : {} : {}]\tReg: {}'.format(current, arg0, arg1, arg2, arg0_d, arg1_d, arg2_d, reg))
            arg0 = arg1 = arg2 = arg0_d = arg1_d = arg2_d = current = reg = ''
        except ValueError: # somehow reg got jumped out of turn
            pass
            #print(current, arg0, arg1, arg2, arg0_d, arg1_d, arg2_d, reg)
    elif 'call' in line and 'sub_401000' in line:
        continue # getting the register should be the last step, not the call.
        #print('0x{}\tsub_401000({:04x}, {:04x}, {:04x})\t[{} : {} : {}]\tReg: {}'.format(current, arg0, arg1, arg2, arg0_d, arg1_d, arg2_d, reg))
        #arg0 = arg1 = arg2 = arg0_d = arg1_d = arg2_d = current = reg = ''
    elif 'print' in line:
        print('PRINTF')
    elif 'scanf' in line:
        print('SCANF')
    else:
        print('BROKEN')
        print(line)
        quit()
