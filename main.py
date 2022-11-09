from functions import *

print("""
--------
BINARY <-> HEX <-> DENARY
by Tika (for L6coD1)
--------
""")

while True:
    base = input("WHAT TYPE OF NUMBER ARE YOU INPUTTING? (B, H, D): ").lower()
    value = input("NUMBER: ")
    to   = input("WHAT DO YOU WANT TO CONVERT TO? (B, H, D): ").lower()

    # they want to go from one type to the same? ok?
    if base == to:
        print(value)
        continue

    result = None

    if base == "b" and to == "d":
        result = binaryToDenary(binary=value)
    elif base == "b" and to == "h":
        result = binaryToHex(binary=value, nDigits=2)
    elif base == "h" and to == "b":
        result = hexToBinary(hexString=value)
    elif base == "h" and to == "d":
        result = hexToDenary(hexString=value)
    elif base == "d" and to == "b":
        result = denaryToBinary(denary=value, n_bits=8)
    elif base == "d" and to == "h":
        result = denaryToHex(denary=value, nDigits=2)
    
    # did this work
    if not result[1]:
        print("AN ERROR OCCURRED")
    else:
        print("Result: " + str(result[0]))
    
    print("\n")