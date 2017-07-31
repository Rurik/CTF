import subprocess

import time 
exe = 'a_patched.exe'
header = '\x90\xBE'
footer = '\x00\x00\x00\x90'
data = open(exe, 'rb').read()
for i in range(0, 255):
    code = header + chr(i) + footer
    newdata = data[0:0x11AF] + code + data[0x11B6::]
    #open('brute.exe', 'wb').write(newdata)
    print i
    quit()
    stdout = subprocess.Popen('brute.exe X')
    stdout.wait()
    sys.delete('brute.exe')
    print "======="
    