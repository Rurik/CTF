import os
import sys
root = '/Users/bbaskin/CTF/LabyREnth_2017/Random/2/squashfs-root'

def get_path(path):
    data = open(path, 'r').readlines()
    p = data[-1].strip()
    try:
        if p[0] == '/':
            print(p)
            next = root + p
            get_path(next)
    except IndexError:
        print('[!] No more chains')
        print(data)

get_path(sys.argv[1])
