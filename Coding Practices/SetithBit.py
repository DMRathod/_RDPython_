number = 9
BitNumber = 3

def SetithBit(number, BitNumber):
    BitMask = (1 << (BitNumber-1))
    result = number | BitMask
    return bin(result)


print(SetithBit(number, BitNumber))