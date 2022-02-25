number = 5

def pattern1(number):
    if(number == 0):
        return 1
    pattern1(number-1) # 
    for i in range(number):
        print("*" ,end ="")
    print("")
    # pattern1(number-1) #alt
    

def pattern2(num,number):
    num = 1
    if(num  == number):
        return
    for i in range(num):
        print("*", end = "")
    print("")
    return pattern2(num+1)



pattern1(number)