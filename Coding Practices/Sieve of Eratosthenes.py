# Sieve of Eratosthenes method for finding the prime number till upper limit. 
#space complexity is there.


import math
number = 5

def IsPrime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if(number % i == 0):
            return False
    return True

def Sieve(number):    
    Booleanarr = [False for i in range(number+1)]
    for i in range(2,int(math.sqrt(number))+1):
        if(IsPrime(i) == True):
            for j in range(i*2,number,i):
                Booleanarr[j] = True

    for i in range(2,len(Booleanarr)-1):
        if(Booleanarr[i] ==  False):
            print(i)

Sieve(number)