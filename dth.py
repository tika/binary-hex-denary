nDigits = int(input("No. digits: "))
denary = int(input("Denary: "))

"""
Converts a denary number to a hexadecimal number

Takes in a denary number and the number of digits of the hex number

Returns a tuple of the result 
and whether this result matches the result of the built in Python function
"""
def denaryToHex(denary, nDigits):
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

    return (hexString, hex(denary) == "0x" + hexString.lower().lstrip("0"))

print(denaryToHex(denary, nDigits))