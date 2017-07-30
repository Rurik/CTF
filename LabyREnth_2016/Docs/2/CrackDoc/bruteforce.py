"""Function suchcrypto(sMessage, strKey)
    Dim kLen, x, y, i, j, temp
    Dim s(256), k(256)
    kLen = Len(strKey)
    For i = 0 To 255
        s(i) = i
        k(i) = Asc(Mid(strKey, (i Mod kLen) + 1, 1))
    Next
    j = 0
    For i = 0 To 255
        j = (j + k(i) + s(i)) Mod 256
        temp = s(i)
        s(i) = s(j)
        s(j) = temp
    Next
    x = 0
    y = 0
    For i = 1 To 3072
        x = (x + 1) Mod 256
        y = (y + s(x)) Mod 256
        temp = s(x)
        s(x) = s(y)
        s(y) = temp
    Next
    For i = 1 To Len(sMessage)
        x = (x + 1) Mod 256
        y = (y + s(x)) Mod 256
        temp = s(x)
        s(x) = s(y)
        s(y) = temp
 
        suchcrypto = suchcrypto & (s((s(x) + s(y)) Mod 256) Xor Asc(Mid(sMessage, i, 1))) & ","
    Next
End Function"""

def suchcrypto(sMessage, strKey):
    kLen = x = y = i = j = temp = 0
    s = k = []
    for i in range(0, 256):
        s.append(None)
        k.append(None)
    
    kLen = len(strKey)
    
    for i in range(0, 256):
        s[i] = i
        k[i] = ( strKey[i % kLen])
        
    j = 0
    for i in range(0, 256):
        a = ord(k[i])
        b = ord(s[i])
        print(a, b)
        j = (j + a + b) % 256
        print(j)
        quit()
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
    
    print(s)

        
        
    quit()
    
suchcrypto('PAN', 'General Vidal')