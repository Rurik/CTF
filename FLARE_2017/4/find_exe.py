import struct
import os
 
const = [0x48025287, 0x57D1B2A2, 0x57D2B0F8, 0x49180192, 0x579E9100]
"""
0x48025287 - 17\4\notepad.exe
0x57D1B2A2 - 16\1\challenge1.exe
0x57D2B0F8 - 16\2\dudelocker.exe
0x49180192 - 16\6\khaki.exe
0x579E9100 - 16\3\unknown
"""
 
def check_time(file):
    with open(file, 'rb') as f:
        try:
            f.seek(0x3c)
            pe_offset = struct.unpack("<I", f.read(4))[0]
            f.seek(pe_offset + 8)
            time = f.read(4)
            time = struct.unpack("<I", time)[0]
            if time in const:
                print('%s => %x' % (file, time))
        except:
            pass

 
def main():
    #for file in os.listdir('.'):
    for root, dirs, files in os.walk('.'):
        path = root.split(os.sep)
        for file in files:
            #if file.endswith(".exe"):
               exe = os.path.join(root, file)
               check_time(exe)
 
if __name__ == '__main__':
    main()