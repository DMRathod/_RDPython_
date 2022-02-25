import math
number = 2

#finding is it prime number or not naive approach

def IsPrime(number):
    for i in range(2,number):
        if(number % i == 0):
            return False
    return True

#if you will observe after sqrt every multiplication is repeating. that is why we can just make 
# condition till sqrt(number) 
# for loop condition can be like i < sqrt(number) or i*i < number 
    

def IsPrimeOpti(number):
    for i in range(2,int(math.sqrt(number))+1):
        if(number % i == 0):
            return False
    return True

#Find prime numbers between number A to number B

def FindPrimeInRange(a, b):
    for i in range(a,b+1):
        if(IsPrimeOpti(i) == True):
            print(i)



print(IsPrimeOpti(number))
# print(FindPrimeInRange(10,30))
