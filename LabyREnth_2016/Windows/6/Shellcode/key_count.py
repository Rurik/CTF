count = 0
for c5 in range(12 + 0x2D, 1 + 0x2D, -1): # Month + 0x2D
    for c6 in range(0 + 0x5E, 31 + 0x5E): # Day + 0x5E
        for c7 in range(0 + 0x4B, 24 + 0x4B): # Hour + 0x4B
            for c8 in range(0x42, 0x52):#(5 + 0x42, 6 + 0x42, 10 + 0x42): # dwMajorVersion + 0x42
                for c9 in range(0x3F, 0x4F):#range(0 + 0x3F, 3 + 0x3F): # dwMajorVersion + 0x3F
                    for c10 in range(0x60, 0x70):#(0x69, 0x6A): #FS30 0/1 + 0x69
                        for c11 in range(0, 256): #User Lang + 0x5E, could loop around
                            count += 1
                            if not count % 1000000: print(count)
print (count)
"""
byte 1 is static 'b'
byte 2 is static '0' #0x40116E
byte 3 is static '0'
byte 4 ! is static
byte 5 = GetLocalTime Month (0x07)  + 0x2D = 0x34 '4'
byte 6 = GetLocalTime Day 0x19 "25" + 0x5E = 0x77 'w'
byte 7 = GetLocalTime Hour 0x9   + 0x42 = 0x4B 'K'
byte 8 is GetVersion = 1DB10106. Take 0x06 add 0x3C = = 0x42 'B'
byte 9 is GetVersion = 1DB10106. Take 0x01 add 0x3F = = 0x40 '@'
byte 10 = FS:[30] = 0x01 + 0x69 = 0x6A "j"
byte 11 = 0x04 (default user lang of 0x0400) + 0x5E = 0x62 'b'

Languages: https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693(v=vs.85).aspx
"""

#key = 'b00!4wJB@jb'
#build_sbox(key)
#codebase = (0xBA, 0xAF, 0x4D, 0x55, 0x3C, 0xE3, 0x03, 0x22, 0xB0, 0xDF, 0xF3, 0xD3, 0x57, 0xD0, 0xE1, 0x40, 0xF9, 0x13, 0x1F, 0xBA, 0x8D, 0x12, 0xF1, 0xFF, 0x48, 0xC2, 0x8E, 0x00, 0xFD, 0x54, 0x97, 0x9D, 0x75, 0x71, 0x30, 0x8F, 0x43, 0x28, 0xFE, 0x69, 0x36, 0x47, 0x8F, 0xA2, 0xEF, 0x49, 0x74, 0x7C, 0xE1, 0x4C, 0x6F, 0x4F, 0xD4, 0x82)
#code = ''
#for i in codebase: code += chr(i)
"""
b00!-^KBE
623030212d5e4b424598a8
['P', 'A', 'N', '\xbd', 'A', '\xfe', '~', '\xa6', '\xbe', '\xc4', '\x04', '\xf6', '\xb0', '\xdf', '\xa6', '\x89', '6', '\xac', 'z', 'H', '2', '\xc1', '\xf6', '\x9e', '\x02', '\xf6', '\xe7', '\x88', 'a', '\x03', '%', '\xc9', '\x9f', 'W', '&', '\xe4', '6', '\x9c', '\x16', '\xdb', '\xf2', '\xf8', '\xb2', '\xeb', '\x98', '\x03', '\r', '\xcb', '\x08', '\x12', '\x1e', '\xe2', '\xb7', '\xc4']
b00!-^KBdX
623030212d5e4b42648558
['P', 'A', 'N', 'G', 'r', 's', 'F', 'O', '\xae', '\x84', 'y', 's', '\xa8', '3', 'I', '\xa6', '\x90', '#', '#', '6', 'd', '\x12', 'x', '\xa5', '\xa5', '\xe3', '\xa8', 'X', '\xa0', 'T', '\xbe', '\xbe', '\x7f', '|', '\xb0', '\xaf', 'm', '\xe6', '\x9b', 'M', '\x13', '\x8c', '\x07', '\xab', '\xd9', 'K', 'z', 'x', '\xec', 'A', 'D', '\x91', '\x01', '.']
b00!-^VPCg
623030212d5e5650436795
['P', 'A', 'N', '\xac', '\x15', '\xb1', 'p', 'p', '\xce', '\x06', '\x1f', '\xb2', '\x8e', '~', "'", '$', 'v', '\x8f', '\x89', '\xf1', '\x0e', '?', '\xe2', '\xb7', '\x06', '\xed', '\x00', '\x97', '\xca', '\xff', '|', '\x86', '\xe0', 'm', 'E', 'V', ')', '\x9a', '?', '\x07', '\xb2', 'A', '\r', '\x10', '\xe4', '\xd4', 'M', 'i', '8', 'K', '\x94', '\xc3', 'i', '\xbe']
b00!-^bJ@ki
623030212d5e624a406b69
['P', 'A', 'N', '\xa9', 'V', '6', '\x88', '\x14', '\x1d', 'z', '\xf0', '\xe1', '\x83', '\x8b', 'p', '\xaf', 'G', 'o', '\xd3', '\x14', '\xd5', 'p', 'f', '!', '\xfe', '\x85', 'y', '\xf5', ';', 'q', '\\', '\x81', 'n', 's', '#', 'T', '&', '\xf4', 'F', '\xe1', '\xbe', '\x84', '\x82', '\xcb', '\xb9', '\xb9', '\xb4', '\xa8', '\xba', 'g', '#', ';', '\xb4', '\x02']
b00!-_RKKj
623030212d5f524b4b6abf
['P', 'A', 'N', '\x1a', '\xf4', '\xb3', '\xb2', 'u', '\xc6', '\xc5', '\xc4', '\x1d', '\xc1', '\x84', 'i', ';', 'h', '\xdb', 'y', '\x9b', '\x1d', 'K', '\xbd', '\xbe', '\x18', '&', '\xd0', '\x0c', '\x80', 'h', '\xb9', '\xbe', '\xd6', '\xbb', '\x02', 'm', 'o', 'l', '\xea', '\x8e', '>', 'Q', '\xd8', '\xfd', '[', '\xa3', ',', '\x03', '\xe1', '\xb6', '\xa0', '\xd5', '\x0c', '\x11']

"""