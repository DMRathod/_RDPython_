# sort will sort each part one by one starting from 0.

#63254
#36254
#23654
#23564
#23456


ns = [6, 13, 2, 18, 4, 1, 12, 17, 3, 5, 9, 15, 90, 23, 40, 45]


def IS(ns):
    i = 0
    j = 0
    temp = 0
    while(i < len(ns)-1):
        j = i + 1 
        if(ns[i] > ns[j]):
            temp = ns[i]
            ns[i] = ns[j]
            ns[j] = temp
            i += 1
            j -= 1
            while(j != 0):
                if(ns[j] < ns[j-1]):    
                    temp = ns[j]
                    ns[j] = ns[j-1]
                    ns[j-1] = temp
                    j -= 1
                else:
                    break
        else:
            i += 1
    return ns
        



print(IS(ns))