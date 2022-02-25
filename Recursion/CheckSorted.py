ns = [1,2,3,4,5,67,89,99]

def CheckSorted(ns, i):
    if(i == len(ns)-1):
        return True
    # if(ns[i] < ns[i+1]):
    return (ns[i] < ns[i+1]) and CheckSorted(ns, i+1)
    # return False

print(CheckSorted(ns,0))