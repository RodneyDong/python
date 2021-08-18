"""
Bitwise Operator: 
& : bit and
| : bit or
^ : bit xor
<<: left shift
>>: right shift

Computer has nothing but electronic switch (on/off or 1/0).
each bit in memory is a switch which represent a binary 1 or 0.
each byte in memory holds 8 bits, int holds 4 bytes, float holds 8 bytes or more.
you can do bitwise operator on byte, int, ...
"""
def binFormat(num):
    s = str(bin(num))
    s1 = s[:2] + s[2:].zfill(8)
    return s1

# define a byte
a = 0b00101100 # 1 byte = 8 bits
print(binFormat(a))
b = 0b00001111 # 1 byte = 8 bits
print(binFormat(b))
print()

# & operator, return 1 if both bit is 1, return 0 otherwise
c = a & b
print(binFormat(a),'&')
print(binFormat(b))
print(binFormat(c))
print()

# | operator: return 1 as long as one is 1, return 0 if both 0
c = a | b
print(binFormat(a),'|')
print(binFormat(b))
print(binFormat(c))
print()

# ^ operator: return 1 if different, return 0 if same
c = a ^ b
print(binFormat(a),'^')
print(binFormat(b))
print(binFormat(c))
print()

# << left shift operator: move all bits to the left, fill 0 on the end
c = a<<1 # move only 1 bit, equivalent to c = a * 2
print(binFormat(a),'<<')
print(binFormat(c))
print()

# >> right shift operator: move all bits to the right, fill 0 on the begining
c = a>>1 # move only 1 bit, equivalent to c = a / 2
print(binFormat(a),'>>')
print(binFormat(c))

a = 'A'

