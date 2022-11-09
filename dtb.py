n_bits = int(input("No. bits: "))
denary = int(input("Denary: "))

"""
Converts a denary number to a binary number

Takes in a denary number and the number of bits of the binary number

Returns a tuple of the result 
and whether this result matches the result of the built in Python function
"""
def denaryToBinary(denary, n_bits):
    if denary > 2 ** n_bits:
        exit("This number is too large for this number of bits")

    binary = ""
    z = denary

    for x in range(n_bits - 1, -1, -1):
        col_val = 2**x
        
        y = z // col_val
        binary += str(y)
        z -= y * col_val

    return (binary, bin(denary) == "0b" + binary)

print(denaryToBinary(denary, n_bits))