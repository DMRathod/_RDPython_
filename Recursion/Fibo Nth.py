
#this function will print Nth fibbo series number.x
#num should be +ve
def fiboNth(num):
    if(num < 2):
        return num
    else:
        return fiboNth(num-1) + fiboNth(num - 2)


print(fiboNth(10))
