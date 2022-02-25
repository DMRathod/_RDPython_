import numbers


number = 41


def step(number):
    print(stp(number, 0))    
      

def stp(number, cnt):
    if(number == 0):
        return cnt
    if(number & 1 == 0):
        return stp(number // 2, cnt + 1)
    else:
        return stp(number - 1, cnt + 1)



print(step(number))