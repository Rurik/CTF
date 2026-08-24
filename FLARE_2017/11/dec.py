from __future__ import print_function

import array
import itertools
from ctypes import c_int32
from struct import unpack

EXE_PATH = 'covfefe.exe'
MEM_SIZE  = 0x1200       # Making sure we don't go out of bounds
OPCODE_START = 0x463
OPCODE_STOP  = 0x1100
SCAN_FLAG  = 3           # instruction slot 3 triggers scanf
SCAN_HOLD  = 1           # instruction slot 1 is input byte
ALPHABET   = 'abcdefghijklmnopqrstuvwxyz_'
MAX_STEPS = 150000   # make sure it doesn't get stuck in infinite loop

def run_code(base_mem, test_code_bytes):
    mem = array.array('i', base_mem)
    opcode = OPCODE_START
    test_code = list(test_code_bytes)
    # Index of the check firing that must show ac1 == ac2.
    checksum_target = max(0, len(test_code) // 2 - 1)
    count = 0
    step = 0

    while opcode + 3 <= OPCODE_STOP and step < MAX_STEPS:
        step += 1
        a1 = mem[opcode]
        a2 = mem[opcode + 1]
        a3 = mem[opcode + 2]

        if a1 < 0 or a1 >= MEM_SIZE:
            break
        if a2 < 0 or a2 >= MEM_SIZE:
            break

        ac1 = mem[a1]
        ac2 = mem[a2]
        value = c_int32(ac2 - ac1).value
        mem[a2] = value

        # Pretend to be scanf
        if a2 == SCAN_FLAG and value == 1 and test_code:
            mem[SCAN_HOLD] = test_code.pop(0)

        # Check if ac1 == ac2
        if opcode == 0x0DFB:
            if count == checksum_target:
                return ac1 == ac2
            if ac1 != ac2:
                return False
            count += 1

        opcode = a3 if (a3 and value <= 0) else opcode + 3

    return False


def main(argv=None):
    max_len = 50 # arbitrary number
    
    # Read the .data section
    with open(EXE_PATH, 'rb') as f:
        content = f.read()
    # .data section at raw file offset 0xa00; instruction starts +8
    mem = array.array('i', [0] * MEM_SIZE)
    base = 0xa08
    for i in range(MEM_SIZE):
        off = base + 4 * i
        if off + 4 <= len(content):
            mem[i] = unpack('<i', content[off:off + 4])[0]
    base_mem = mem

    recovered = []
    while len(recovered) < max_len:
        found = None

        if len(recovered) + 2 <= max_len:
            for guess in itertools.product(ALPHABET, repeat=2):
                test_code = bytes(recovered + [ord(c) for c in guess])
                if run_code(base_mem, test_code):
                    found = [ord(c) for c in guess]
                    break

        if not found and len(recovered) + 1 <= max_len:
            for ch in ALPHABET:
                test_code = bytes(recovered + [ord(ch)]) + b'\n'
                if run_code(base_mem, test_code):
                    found = [ord(ch)]
                    break

        if not found:
            break

        recovered.extend(found)
        password_temp = ''.join(chr(c) for c in recovered)
        print(password_temp)

    password = ''.join(chr(c) for c in recovered)

    print('Password: %s' % password)
    return 0

if __name__ == '__main__':
    main()
