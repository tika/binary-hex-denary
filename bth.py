nDigits = int(input("No. digits: "))
binary = input("Binary: ")

"""
Converts a binary number to a hexadecimal number

Takes in a binary number

Returns a tuple of the result 
and whether this result matches the result of the built in Python function
"""
def binaryToHex(binary):
    # convert binary to denary
    total = 0

    for k in range(len(binary) - 1, -1, -1):
        col_val = 2**k
        total += int(binary[len(binary) - 1 - k]) * col_val
    
    if total > 16 ** nDigits:
        exit("This number is too large for this number of digits")


    # convert total to hex
    hexStore = ["A", "B", "C", "D", "E", "F"]
    hexArray = []

    for _ in range(nDigits):
        remainder = total % 16
        wholePart = total // 16
        
        if remainder >= 10:
            hexArray += [str(hexStore[remainder - 10])]
        else:
            hexArray += [str(remainder)]
        
        total = wholePart

    hexString = "".join(reversed(hexArray))

    return (hexString, int(hexString, base=16) == int(binary, base=2))

print(binaryToHex("11111010"))