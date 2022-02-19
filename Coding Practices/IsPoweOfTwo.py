#first approach for this question is to check wether in 
#binary representation of that number is having only 1 digit as 1 or not. for that we have 
#to run the loop till we didn't find 2nd 1. if we didn't find 2nd 1 then it is power of 2.
# 
# 
# 
# 
# second approach for this question is as below we will use bitwise & operator to find out is 
# it power of 2 or not.  


#take number > 0

number = 16

def IsPowerOfTwo(number):
    result = (number & (number -1)) == 0
    return result

print(IsPowerOfTwo(number))