#this program is finding the factor of the given number 

import math


number = 84
def Factors(number):    
    for i in range(1, int(math.sqrt(number))+1):
        if((number/i) == i):
            print(i , end = " ")
        else:
            if(number % i == 0):
                print(i, int(number/i), end = " ")

Factors(number)
