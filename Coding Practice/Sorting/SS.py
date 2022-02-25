ns = [4, 5, 1, 22]

# selection sort will just find the one element and put that element at its right position
# here i have taken max element and putting at its right psition each time in each iteration


# def SSort(ns):
#     for i in range(len(ns)):
#         mx = ns[0]
#         j = 1
#         k = 0
#         while(j < len(ns)-i):
#             if(mx < ns[j]):
#                 mx = ns[j]
#                 k = j
#             j += 1
#         temp = ns[j-1]
#         ns[j-1] = ns[k]
#         ns[k] = temp
#     return ns

def SSortREC(ns,j):
    if(j == 0):
        return ns
    m = 0
    mx = 0
    for i in range(len(ns)):
        if(mx < ns[i]):
            mx = ns[i]
            m = i
    temp = ns[i-1]
    ns[i-1] = ns[m]
    ns[m] = temp
     
    return SSortREC(ns,j-1) 
  
print(SSortREC(ns,0))
        