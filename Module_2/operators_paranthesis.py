print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
#1    ((5 * ((12) + 100) / (26)) // 2)
#2    ((5 * (112) / (26)) // 2)
#3    ((560 / (26)) // 2)
#4    ((21.538) // 2)
#5    (10.0)

# At Step 2, order of operations kicks in from LEFT to RIGHT
# Thus, 5 * 112

print((2 ** 4), (2 * 4.), (2 * 4))
# ((16), (8.0), (8))

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
# ((-.5), (.5), (0), (-1))
# -2 // 4 rounds DOWN to -1

print((2 % -4), (2 % 4), (2 ** 3 ** 2))
# ((-2), (2), (512))
# Ex 2: 4 goes into 2 ZERO times, thus the remainder is 2.
# Ex 1: Since the divisor is -4, the output is -2
