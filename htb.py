hexString = input("Hex: ")

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

print(hexToBinary(hexString))