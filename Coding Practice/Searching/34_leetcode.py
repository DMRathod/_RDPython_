# nums = [1, 2, 4, 4, 4, 5, 5, 6]
# nums = [5,7,7,8,8,10]
# nums = [5,7,7,8,8,10]
nums = [1,2,3,4,5,6]

def test(nums, target):
    s = 0
    e = len(nums)-1
    p = -1
    m = -1
    cnt  = 0
    if(nums == []):
        return [p, p]

    while(s <= e ):
        m = (s+e) // 2
        if(nums[m] == target):
            p = m
            break
        if(nums[m] < target):
            s = m + 1
        else:
            e = m - 1
    l = p
    if(p != -1):  
        while( p != 0 and nums[p-1] == nums[p]):
            p -= 1
            if(p == 0):
                break
        
        while( l != len(nums)-1 and nums[l+1] == nums[l] ):
            l += 1
            if(l == len(nums)-1):
                break
    return [p, l]
    



print(test(nums,1))