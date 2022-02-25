ns = [4,3,2,1]

# compare 2 elements if first one is larger swap it. in first pass max element will be set to end position
# second pass second max element will be at second last position
# third pass third max element will be at third last position and so on...

def BSort(ns):
    temp = 0
    for j in range(len(ns)):
        i = 1    
        while(i < len(ns)-j):
            if(ns[i-1] > ns[i]):
                temp = ns[i]
                ns[i] = ns[i-1]
                ns[i-1] = temp 
            i += 1
    return ns

print(BSort(ns))