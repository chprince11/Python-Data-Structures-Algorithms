# Convert Decimal to Binary

deciToBin = bin(5)
print(deciToBin) #0b101

deciToBin = bin(5)[2:] # removing 2 digit from begining
print(deciToBin) #101

# Convert Binary to Decimal

binary_5 = '101'
BinToDeci = int(binary_5, 2)
print(BinToDeci) #5

# Bitwise AND operator ( & )

print ( 5 & 7 ) #5

# Bitwise OR operator ( | )

print ( 5 | 7 ) #7

# Bitwise XOR operator ( + inside a circle or ^ )

print ( 5 ^ 7 ) #2

# Bitwise NOT operator ( ~ )

print ( ~5 ) #-6

# Left shift ( << )

print ( 5 << 2 ) #20

# Arithmetic (Signed) Right shift ( << )

print ( 5 >> 1 ) #2

# Hexadecimal (Base 16)
""" 
0 0 
1 1
2 2
...
10 a
11 b
...
14 e
15 f
"""

print(hex(5)) # 0x5
print(hex(16)) # 0x10
print(hex(17)) # 0x11
print(hex(12)) # 0xc
print(hex(25)) # 0x19  ( 1* 16^1 + 9 * 16^0 = 16 + 9 = 25)
