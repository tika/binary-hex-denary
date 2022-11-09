"""
Converts a hexadecimal number to a denary number

Takes in a hexadecimal number

Returns a tuple of the result 
and whether this result matches the result of the built in Python function
"""
def hexToDenary(hexString):
    total = 0
    hexStore = ["A", "B", "C", "D", "E", "F"]
    for x in range(len(hexString) - 1, -1, -1):
        current = hexString[x]
        number = 0
        if current in hexStore:
            number += 10 + hexStore.index(current)
        else:
            number += int(current)
        total += (16 ** x) * number
    return (total, int(hexString, base=16) == total)

"""
Converts a hexadecimal number to a binary number

Takes in a hexadecimal number

Returns a tuple of the result 
and whether this result matches the result of the built in Python function
"""
def hexToBinary(hexString):
    binary = ""
    hexStore = ["A", "B", "C", "D", "E", "F"]

    # Take 1 digit and convert to 4 bits
    for x in hexString:
        nibble = ""
        value = 0

        if x in hexStore:
            value = 10 + hexStore.index(x)
        else:
            value = int(x)


        # convert value to binary
        for k in range(3, -1, -1):
            col_val = 2**k

            y = value // col_val
            binary += str(y)
            value -= y * col_val
        
        binary += nibble

    return (binary, int(binary, base=2) == int(hexString, base=16))

"""
Converts a denary number to a hexadecimal number

Takes in a denary number and the number of digits of the hex number

Returns a tuple of the result 
and whether this result matches the result of the built in Python function
"""
def denaryToHex(denary, nDigits):
    denary = int(denary)

    if denary > 16 ** nDigits:
        exit("This number is too large for this number of digits")

    hexStore = ["A", "B", "C", "D", "E", "F"]
    hexArray = []
    count = denary

    for _ in range(nDigits):
        remainder = count % 16
        wholePart = count // 16
        
        if remainder >= 10:
            hexArray += [str(hexStore[remainder - 10])]
        else:
            hexArray += [str(remainder)]
        
        count = wholePart

    hexString = "".join(reversed(hexArray))

    return (hexString, denary == int(hexString, base=16))

"""
Converts a denary number to a binary number

Takes in a denary number and the number of bits of the binary number

Returns a tuple of the result 
and whether this result matches the result of the built in Python function
"""
def denaryToBinary(denary, n_bits):
    denary = int(denary)

    if denary > 2 ** n_bits:
        exit("This number is too large for this number of bits")

    binary = ""
    z = denary

    for x in range(n_bits - 1, -1, -1):
        col_val = 2**x
        
        y = z // col_val
        binary += str(y)
        z -= y * col_val

    return (binary, denary == int(binary, base=2))

"""
Converts a binary number to a hexadecimal number

Takes in a binary number and the number of digits of the resultant hex number

Returns a tuple of the result 
and whether this result matches the result of the built in Python function
"""
def binaryToHex(binary, nDigits):
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

"""
Converts a binary number to a denary number

Takes in a denary number and the number of bits of the binary number

Returns a tuple of the result 
and whether this result matches the result of the built in Python function
"""
def binaryToDenary(binary):
    denary = 0

    for x in range(len(binary)):
        col_val = 2 ** x
        denary += col_val * int(binary[len(binary) - x - 1])

    return (denary, int(binary, base=2) == denary)