elements = [1, 2, 3, 44, 55, 66, 76]

def BinarySearch(elements, start, end, target):
    if(start > end):
        return -1
    m = (start+end)//2
    if(elements[m] == target):
        return m
    if(target > elements[m]):
        return BinarySearch(elements, m+1, end, target)
    return BinarySearch(elements, start, m-1, target)

print(BinarySearch(elements, 0, len(elements)-1, 77))

