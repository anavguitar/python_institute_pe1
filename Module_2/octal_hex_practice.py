"""
Exercises: Decimal to Octal/Hexadecimal
Translate the following decimal numbers to their octal and hexadecimal equivalents:
Decimal 12
Decimal 27
Decimal 100
Decimal 255
Decimal 400
"""
print("DECIMAL TO OCT AND HEX")
# Decimal 12
twelve_oct = 0o14
twelve_hex = 0xb
print(twelve_oct, twelve_hex)
# Decimal 27
twentySeven_oct = 0o33
twentySeven_hex = 0x1b
print(twentySeven_oct, twentySeven_hex)
# Decimal 100
hundred_oct = 0o144
hundred_hex = 0x64
print(hundred_oct, hundred_hex)
# Decimal 255
twoFiftyFive_oct = 0o377
twoFiftyFive_hex = 0xff
print(twoFiftyFive_oct, twoFiftyFive_hex)
# Decimal 400
fourHundred_oct = 0o620
fourHundred_hex = 0x190
print(fourHundred_oct, fourHundred_hex)

"""
Exercises: Octal/Hexadecimal to Decimal
Translate the following numbers to their decimal equivalents:
0o25
0o100
0o777
0x1A
0x50
0xFF
0x100
"""
print("OCTAL AND HEX TO DECIMAL")

dec_0o25 = 21
print(0o25, 21)
dec_0o100 = 64
print(0o100, 64)
dec_0o777 = 511
print(0o777, 511)
dec_0x1A = 26
print(0x1A, 26)
dec_0x50 = 80
print(0x50, 80)
dec_0xFF = 255
print(0xFF, 255)
dec_0x100 = 256
print(0x100, 256)
