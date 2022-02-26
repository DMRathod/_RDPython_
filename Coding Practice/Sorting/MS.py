ns1 = [3]
ns2 = [1]
ns = [1,15,6,17,2,3,5,6]
#iterative 

def MSdevide(ns):
    if(len(ns) ==  1):
        return ns

    m = len(ns) // 2
    left  = ns[0:m]
    right = ns[m:]
    left  = MSdevide(left)
    right = MSdevide(right)

    return MSmerge2(left, 0, right, 0)

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
print(MSdevide(ns))