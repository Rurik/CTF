import array


def suchcrypto(sMessage, strKey):
    s = array.CreateInstance(256)
    k = array.CreateInstance(256)
    kLen = Len(strKey)
    i = 0
    while i <= 255:
        s[i] = i
        k[i] = Asc(Mid(strKey, (i % kLen) + 1, 1))
        i = i + 1
    j = 0
    i = 0
    while i <= 255:
        j = (j + k(i) + s[i]) % 256
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i = i + 1
    x = 0
    y = 0
    i = 1
    while i <= 3072:
        x = (x + 1) % 256
        y = (y + s[x]) % 256
        temp = s[x]
        s[x] = s[y]
        s[y] = temp
        i = i + 1
    i = 1
    while i <= Len(sMessage):
        x = (x + 1) % 256
        y = (y + s[x]) % 256
        temp = s[x]
        s[x] = s[y]
        s[y] = temp
        suchcrypto = suchcrypto + (s((s[x] + s[y]) % 256) ^ Asc(Mid(sMessage, i, 1))) + ","
        i = i + 1
            
            
print(suchcrypto("P", "General Vidal"))