
import math
 

#recursive approach 
def SumOfdigit(number):
    if(number == 0):
        return 0
    r = (number % 10)
    number = number // 10
    return r + SumOfdigit(number)


#iterative approach
def SumOfdigit_(number):
    result = 0
    while(number  > 0):
        result += (number % 10)
        number = number // 10
    return result    


#recursive for multiplication of digit
def MulOfdigit(number):
    if(number == 0):
        return 1
    r =  number % 10 
    return r * MulOfdigit(number//10)


result = 0
def ReverseNumber(number):
    if(number == 0):
        return
    global result
    r = number % 10
    result = r + result*10
    ReverseNumber(number // 10)
    

def ReverseREC(number, digit):
    if(number %10 == number):
        return number
    r = number % 10
    return r*int(pow(10,digit-1)) + ReverseREC(number//10, digit-1)

def CountZero(number):
    cnt = 0
    while(number > 0):
        r = number % 10
        if(r == 0):
            cnt += 1 
        number = number // 10
    return cnt 

def CountZeroREC(number, cnt):
    if(number == 0):
        return cnt
    r = number % 10
    if(r == 0):
        cnt += 1
    return CountZeroREC(number // 10, cnt)

def SendZeroToEnd(number):
    digit =  int(math.log10(number)) + 1
    mul = 1
    result = 0
    while(number > 0):
        r = number % 10
        if( r != 0 ):
            #result = result*10 + r  #if we need reverse number and then append zero
            result += r*mul
            mul *= 10
        number = number // 10
    return result* pow(10,digit - (int(math.log10(result))+1))
        



    




number = 20340
digit = int(math.log10(number)) + 1

#check if reverse is same then number is palindrome.

print(SendZeroToEnd(number))