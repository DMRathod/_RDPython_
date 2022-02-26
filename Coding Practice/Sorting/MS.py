ns1 = [3]
ns2 = [1]
ns = [1,17,2,3,5,6]

# sort will deivide array in 2 parts till one element left and then it will 
# merge in sorted manner.



#iterative 
def MSdevide(ns, s, e):
    if(len(ns) == 1):
        return ns
    # if( e-s == 1):
    #     return 
    


    # m = len(ns) // 2
    m = (s+e) // 2
    left  = ns[0:m]
    right = ns[m:]
    left  = MSdevide(ns, 0, m)
    right = MSdevide(ns, m , len(ns))
    # MSdevide(ns, s, m)
    # MSdevide(ns, m , e)
    return MSmerge1(left, right)
    # return MSmergeInplace(ns, s, m, e)

# def MSmergeInplace(ns, s, m, e):
#     nss = []
#     i = s
#     j = m
#     while(i < m and j < e):
#         if(ns[i] < ns[j]):
#             nss.append(ns[i])
#             i += 1
#         else:
#             nss.append(ns[j])
#             j += 1
#     if(i == m):
#         for l in range(j, e):
#             nss.append(ns[l])
#     if(j == e):
#         for k in range(i,m):
#             nss.append(ns[k])

#     for p in range(s,len(nss)):
#         ns[s+p] = nss[p]
    
def MSmerge1(ns1, ns2):
    i = 0 
    ns = []
    j = 0 
    while(i < len(ns1) and j < len(ns2)):
        if(ns1[i] > ns2[j]):
            ns.append(ns2[j])
            j += 1 
        else:
            ns.append(ns1[i])
            i += 1
    if(j == len(ns2)):
        for l in range(i,len(ns1)):
            ns.append(ns1[l])
    if(i == len(ns1)):
        for k in range(j,len(ns2)):
            ns.append(ns2[k])
    return ns
           
#recursive

def MSmerge2(ns1, i, ns2, j):
    ns = []
    nsq = []
    if(i == len(ns1)):
        for k in range(j, len(ns2)):
            ns.append(ns2[k])
        return ns
    if(j == len(ns2)):
        for l in range(i, len(ns1)):
            ns.append(ns1[l])
        return ns
    if(ns1[i] < ns2[j]):
        ns.append(ns1[i])
        nsq =  MSmerge2(ns1, i+1, ns2, j)
        ns.extend(nsq)
        return ns
    else:
        ns.append(ns2[j])
        nsq = MSmerge2(ns1, i, ns2, j+1)
        ns.extend(nsq)
        return ns 

# print(MS1(ns1, 0, ns2, 0))
print(MSdevide(ns, 0, len(ns)))
print(ns)