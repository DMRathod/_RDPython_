number = 36

def sqrt(number, precision):
    s = 0
    e = number
    result = 0.0
    # m = (s+e) // 2
    while(s <= e):
        m = (s+e) // 2
        if(m*m == number):
            return m
        if(m*m > number):    
            e = m - 1 
        else:
            s = m + 1
    result = m
    print(result)
    incr = 0.1
    for i in range(precision):
        while(result*result < number):
            result += incr
        result -= incr
        incr /= 10
    return result 

        

print(sqrt(number,2))    






