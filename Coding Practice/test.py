# nums = [1, 2, 4, 4, 4, 5, 5, 6]
# nums = [5,7,7,8,8,10]
nums = [1,2,3]

def test(nums, target):
    s = 0
    e = len(nums)
    p = 0
    cnt  = 0
    while(s < e):
        m = (s+e) // 2
        if(nums[m] == target):
            p = m
        if(nums[m] < target):
            s = m + 1
        else:
            e = m - 1
    
    # if(p == 0):
    #     return [0, 0]
    # while(nums[p-1] == nums[p] and p != 0):
    #     p -= 1

    # l = p
    # if(p == len(nums) - 1):
    #     return [p, p]
    
    # while(nums[l+1] == nums[l] and l != len(nums)):
    #     l += 1
    
    # return [p, l]
    return p


print(test(nums,1))