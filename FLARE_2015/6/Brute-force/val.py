def decode(KEY):
  #memcpy(CIPHER, &off_5004, 92)

  data = open('cipher.dat', 'rb').read()
  print len(data)
  print data[0]
  s = []
  for i in range(0, len(data)):
    print i,
    s[i] = ord(data[i])
  CIPHER = open('cipher2.dat', 'rb').read()
  if KEY and len(KEY) <= 46:
    OUTPUT_POS = 0;
    v15 = 1;
    for i in range(0, len(KEY), 2):

      v4 = 0;
      if ( KEY[i] ):
        v4 = KEY[i]
        if ( KEY[i + 1] ):
#          v4 = &unk_7E7E >= ((KEY[i] << 8) | KEY[i + 1]) ? (KEY[i] << 8) | KEY[i + 1] : 0;
            v4 = 1
      WORD_POS = 0;
      for WORD_POS in range(0, 6952, 2):
        v16 = ord(CIPHER[WORD_POS])
        print v4, v16
        while ( not (v4 % v16 & 0xFFFF) ):
          s[WORD_POS] += 1  #++(&s + WORD_POS);
          v4 = v4 / v16 & 0xFFFF
          if ( v4 <= 1 ):
            break


  else:
    v8 = 123#(const char *)&unk_3D3C;
    print "v8 123"
  return 


print decode('sdfsdfsdf@flare-on.com')