#1 - 001 - 5
#2 - 010 - 25
#3 - 011 - 30
#4 - 100 - 125
#find magic number for n.
#complexity of this prgram is log(n) becasue loop is running for number 
#of digits in the binary representation of the number.


number = 18

def MagicNumber(number):
    base = 5
    result = 0
    while(number > 0):
        rsb = (number & 1)  #finding the right least significant bit
        number = number >> 1 #right shifting the lsb by one
        result += rsb*base
        base = base*5
    return result



print(MagicNumber(number))



