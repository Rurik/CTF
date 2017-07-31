import dpkt
import base64

f = open('challenge.pcap', 'rb')
pcap = dpkt.pcap.Reader(f)
fnames = ''
results = list()

for ts, buf in pcap:
    try:
        eth = dpkt.ethernet.Ethernet(buf)
    except:
        continue
        
    if eth.type != 2048:  # Not UDP
        continue
        
    ip = eth.data
    
    udp = ip.data
    if udp.sport != 53 and udp.dport != 53:
        continue
    
    try:
        dns = dpkt.dns.DNS(udp.data)
    except dpkt.dpkt.UnpackError:
        # "Valid" packets show under unparsable DNS response 
        data = udp.data
        a = data.split(b'\x03')[0]
        b = a.split(b'\xc0')
        c = b[2].split(b'\x02')[0]
        results.append(c) 
    
final = b''
for i in results: 
    final += i[1::]
print(final)
open('output.zip', 'wb').write(base64.b64decode(final))