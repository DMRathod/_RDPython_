ns = [1, 23, 45, 34, 2, 34, 45, 56]

def IsExist(ns, target, i):
    if(i == len(ns)-1):
        return False
#    if(ns[i] == target):
 #       return True
    return ns[i] == target or Exist(ns, target, i+1)

def IsExist_(ns, target):
    i = 0
    while(i != len(ns)-1):
        if(ns[i] == target):
            return True
        else:
            i += 1 
    return False


def IsExist__(ns, target, i):
    l = []
    if(i == len(ns)-1):
        return l 
    if(ns[i] == target):
        l.append(i) 
    l1 =  IsExist__(ns, target, i+1)
    l.extend(l1)
    return l 


print(IsExist__(ns, 34, 0 ))