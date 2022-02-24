#first we need to think power in binary representation then if bit is 1 then add that base 
#into actual result otherwise then each time you need to right shift power.


base = 3
power = 2

def FindPower(base, power):
    result = 1
    while(power > 0): 
        if((power & 1) == 1):
            result *= base 
        base *= base
        power = (power >> 1)
    return result

print(FindPower(base, power))


