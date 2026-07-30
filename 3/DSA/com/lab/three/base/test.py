#!/usr/bin/env python3
# gray_bcd_decode.py

binary_strings = [
    "0011 0100",
    "0011 0011",
    "0010 0110",
    "0101 0001",
    "0001 0010",
    "0010 0011",
    "0100 0011",
    "0100 0001",
    "0011 0110",
    "0011 0011",
    "0001 0011",
    "0010 0101",
    "0100 0001",
    "0101 0011"
]

def gray_to_bin(g):
    b = g
    while g > 0:
        g >>= 1
        b ^= g
    return b

def bits_to_int(bits):
    return int(bits, 2)

decoded_nibbles = []

for s in binary_strings:
    hi, lo = s.split()
    hi_val = bits_to_int(hi)
    lo_val = bits_to_int(lo)
    # Convert Gray to Binary
    hi_decoded = gray_to_bin(hi_val)
    lo_decoded = gray_to_bin(lo_val)
    decoded_nibbles.append((hi_decoded, lo_decoded))

print("--- Gray → Binary decoded nibbles ---")
for (h, l) in decoded_nibbles:
    print(f"{h:04b} {l:04b}  ->  ({h}, {l})")

# Recombine into bytes
decoded_bytes = [h << 4 | l for (h, l) in decoded_nibbles]
print("\nDecoded bytes (hex):", [f"{b:02X}" for b in decoded_bytes])

# Try interpret as ASCII (latin1)
as_ascii = bytes(decoded_bytes).decode('latin1')
print("Decoded ASCII:", as_ascii)

# Also interpret as BCD digits (if <=9)
maybe_bcd = [str(h) + str(l) for (h, l) in decoded_nibbles if h <= 9 and l <= 9]
if maybe_bcd:
    print("Decoded as BCD string:", ''.join(maybe_bcd))
