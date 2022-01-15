num =  [12, 23, 34, 45, 54, 67, 78, 99]

def BS(num, target, s, e):
    if(s >= e):
        return -1
    m = s+ (e-s) // 2
    if(num[m] == target):
        return m
    if(num[m] > target):
        return BS(num, target, 0, m-1)
    return BS(num, target, m+1, len(num))



print(BS(num, 99, 0, len(num))) // 7

