#find ith bit of the binary string of this number
number = 127
BitNumber = 18

def FindithBit(number, BitNumber):
    BitMask = (1 << (BitNumber-1))
    ithBit = BitMask & number
    if(ithBit == 0):
        return 0
    else:
        l = list(bin(ithBit))
    return l[-BitNumber]


print(FindithBit(number, BitNumber))