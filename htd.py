hexString = input("Hex: ")

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

print(hexToDenary(hexString))