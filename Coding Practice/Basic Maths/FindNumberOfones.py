number = 1272

#simple approach 
#log(n)

print(str(bin(number)))
def FindNumberofones(number):
    cnt = 0
    while(number > 0):
        if((number & 1) == 1):
            cnt += 1
        number = number >> 1
    return cnt

# print(FindNumberofones(number))



#Very optimized approach
#log(number of ones)

def FindNumberofones_(number):
    cnt = 0
    while(number > 0):
        cnt +=1
        #number -= number & (-number)
        number = number & (number-1)
    return cnt

print(FindNumberofones_(number))