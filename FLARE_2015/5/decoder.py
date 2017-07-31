import base64
key = 'flarebearstare'
data_base64 = 'UDYs1D7bNmdE1o3g5ms1V6RrYCVvODJF1DpxKTxAJ9xuZW=='.swapcase()
data = base64.b64decode(data_base64)

result = ''
for i in range(0, len(data)):
    result += chr(ord(data[i]) - ord(key[i%14]))
print result