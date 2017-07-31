import os
import sys
root = '/Users/bbaskin/CTF/Labyrenth/Random/1/squashfs-root'
counter = 0

def get_path(path):
    global counter
    counter += 1
    print(counter)
    data = open(path, 'r').readlines()
    print(data)
    p = data[-1].strip()
    if p[0] == '/':
        next = root + p
        #print(next)
        get_path(next)


get_path(sys.argv[1])
