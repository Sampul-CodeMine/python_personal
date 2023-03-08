# Problem:  (9-7)*2**3 + 10%6 // -1*2-1

# First step, bracket: (9-7)*2**3 + 10%6 // -1*2-1 ---- 2*2**3 + 10%6 // -1*2-1
# Second step, exponential: 2*2**3 + 10%6 // -1*2-1 ---- 2*8 + 10%6 // -1*2-1
# Third step, multiplication: 2*8 + 10%6 // -1*2-1 ---- 16 + 10%6 // -1*2-1
# Fourth step, modulus division: 16 + 10%6 // -1*2-1 ---- 16 + 4 // -1*2-1
# Fifth step, floor division:  16 + 4 // -1*2-1 ---- 16 - 4 * 2 -1
# Sixth step, multiplication: 16 - 4 * 2 -1 ---- 16 - 8 -1
# Seventh step, subtraction: 16 - 8 - 1 ---- 8 - 1
# Eight step, subtraction: 8 -1 --- 7
# 7 is the answer

print((9-7)*2**3 + 10 % 6 // -1*2-1)
