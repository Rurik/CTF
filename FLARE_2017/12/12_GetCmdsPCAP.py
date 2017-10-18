import codecs
import struct
import sys
import os
import subprocess
import dpkt
import base64
import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9443
pktcount = 0
packets = []


def handle_client_connection(client_socket):
    global pktcount
    client_socket.send(packets[pktcount])
    print('Send pkt[{}]={}'.format(pktcount, packets[pktcount][0:10]))
    pktcount += 1
    request = client_socket.recv(1024)
    print 'Received {}'.format(request)
    #client_socket.close()


def main():
    global packets

    f = open('20170801_1300_filtered_C2.pcap', 'rb')
    pcap = dpkt.pcap.Reader(f)
    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        tcp = ip.data
        data = tcp.data
        header = tcp.pack_hdr
        # 340068c8 = server
        # c0a8dd5b = victim
        if ip.src == '\x34\x00\x68\xc8':
            try:
                pt2 = data.split('\x17\x04\x17\x20')[1]
                print(codecs.encode(pt2[0], 'hex_codec')),
            except IndexError:
                print('X'),


    print('\nC2 Packets: {}'.format(len(packets)))

if __name__ == '__main__':
    main()
