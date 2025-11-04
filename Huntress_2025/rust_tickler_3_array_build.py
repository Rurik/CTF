from capstone import *
from capstone.x86 import *

CODE = open("0x140001fc0.dat", "rb").read()

md = Cs(CS_ARCH_X86, CS_MODE_64)
md.detail = True

output_array = []

for i in md.disasm(CODE, 0):
    if i.mnemonic == "mov" and len(i.operands) == 2:
        dst, src = i.operands

        # Only handle byte writes to [rbp + disp]
        if (dst.type == X86_OP_MEM and
            dst.mem.base == X86_REG_RBP and
            src.type == X86_OP_IMM and
            i.op_str.startswith("byte ptr")): # no qword ptr
            
            value = src.imm & 0xFF
            output_array.append(value)

open("0x140001fc0_reconstructed.dat", "wb").write(bytes(output_array))
