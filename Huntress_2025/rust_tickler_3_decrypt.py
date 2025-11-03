import struct
import sys

def rol32(value, shift):
    """Rotate left 32-bit"""
    shift &= 0x1f
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def ror32(value, shift):
    """Rotate right 32-bit"""
    shift &= 0x1f
    return ((value >> shift) | (value << (32 - shift))) & 0xFFFFFFFF

def decrypt_str(data, seed):
  result = []

  for i in range(len(data)):
      inv_seed = (~seed) & 0xFFFFFFFF

      rotated_inv = rol32(inv_seed, 4) | 1
      ror_val = ror32(seed, seed & 0xFF)
      new_seed = (rotated_inv + ((ror_val & 0xfffffffc) + 1) * seed) & 0xFFFFFFFF

      shifted = (seed >> (inv_seed & 0xF)) & 0xFFFFFFFFFFFFFFFF
      shift_byte = shifted & 0xFF
      temp = ((shifted * 0xaaaaaaab) >> 0x24) & 0xFFFFFFFF
      shift_amount = (shift_byte - ((temp << 3) * 3)) & 0xFF

      xor_key = (new_seed >> shift_amount) & 0xFF
      result.append(data[i] ^ xor_key)
      seed = new_seed

  return bytes(result)


# Read HNTB.dat
with open('HNTB.dat', 'rb') as f:
    data = f.read()

# Parse 12-byte entries: ID, offset, size
offset = 8
entries = []

while offset + 12 <= len(data):
    entry_id, data_offset, data_size = struct.unpack('<III', data[offset:offset+12])
    if data_offset >= len(data) or data_size > len(data):
        break
    encrypted = data[data_offset:data_offset+data_size]
    entries.append((entry_id, encrypted))
    offset += 12

print(f"Parsed {len(entries)} entries from HNTB.dat\n")

# Decrypt all entries
for entry_id, encrypted in sorted(entries, key=lambda x: x[0]):
    decrypted = decrypt_str(encrypted, entry_id)

    text = decrypted.decode('utf-8', errors='ignore').strip('\x00')
    # Remove any trailing null bytes or unprintable characters
    text = ''.join(c for c in text if c.isprintable() or c in '\n\r\t')

    # Don't print if over 200 bytes
    if len(text) > 200:
        print(f"ID 0x{entry_id:04x}: [text: {len(text)} bytes] ({text[0:16]})")
        fh = open('{}.dat'.format(entry_id), 'wb')
        fh.write(text.encode('utf-8'))
        fh.close()
    else:
        print(f"ID 0x{entry_id:04x}: {text}")

