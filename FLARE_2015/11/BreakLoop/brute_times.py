import subprocess
seconds = 3

for i in range(200, 255):  # Honestly, I broke this up into 6 simultaneous scripts to run faster
    cmd = 'breakme.exe %d' % i
    print(cmd)
    try:
        stdout = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=seconds)
    except subprocess.TimeoutExpired:
        continue
