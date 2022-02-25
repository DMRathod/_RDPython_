def GCD(a, b):
    if(a == 0):
        return b 
    return GCD(b%a ,a)

def LCM(a, b):
    return (a*b)/GCD(a, b)



print(LCM(8 ,6))