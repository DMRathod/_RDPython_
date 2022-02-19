number = 10

#try to find the logic after doing XOR of 0-10 find the pattern for module 4.

def FindXOR_0_to_a_(number):
    if(number % 4 == 0):
        return number
    if(number % 4 == 1):
        return 1
    if(number % 4 == 2):
        return number+1
    if(number % 4 == 3):
        return 0


#we neeed to remove the XOR part of 0 to point a. by doing and willl remove the same part.
# a-1 because we need to include a. 

def FindXOR_range(a, b):
    result = FindXOR_0_to_a_(a-1) ^ FindXOR_0_to_a_(b)
    return result 

print(FindXOR_0_to_a_(number))
print(FindXOR_range(3, 9))
