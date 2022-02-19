def IsOddorEven(number):
    return (number & 1) == 1

if(IsOddorEven(15) ==  True):
    print("Odd")
else:
    print("Even")