#image input
#100
#011
#111

# horizontal flip
# 001
# 110
# 111

# invert 
# 110
# 001
# 000

def swap(arr,i,j):
    arr[i] = arr[i] + arr[j]
    arr[j] = arr[i] - arr[j]
    arr[i] = arr[i] - arr[j]
    return arr

def flipAndInvertImage(image):
    i = 0
    while(i < len(image)):
        ReverseArray(image[i])
        Compliment(image[i])
        i += 1
    return image

#optimized code

def flipAndInvertImage1(image):
    for arr in image:
        i = 0
        j = len(arr)-1
        while(i <= j):
            temp = arr[i] ^ 1 
            arr[i] = arr[j] ^ 1
            arr[j] = temp 
            i +=1
            j -=1
    return image

def ReverseArray(arr):
    i = 0
    j = len(arr) - 1
    while(i < j):
        swap(arr, i, j)
        i += 1
        j -= 1
    return arr

def Compliment(arr):
    for i in range(len(arr)):
        arr[i] ^= 1
    return arr   

image = [[1,1,0],[0,1,0],[0,1,1]]
# S = Solution()
print(image)
# print(flipAndInvertImage(image))
print(flipAndInvertImage1(image))
