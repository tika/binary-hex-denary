binary = input("Binary: ")

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

    return (denary, "0b" + binary == bin(denary))

print(binaryToDenary(binary))