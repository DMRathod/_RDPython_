arr = [1, 2, 3, 4, 5, 6]


def swap(arr,i,j):
    arr[i] = arr[i] + arr[j]
    arr[j] = arr[i] - arr[j]
    arr[i] = arr[i] - arr[j]
    return arr

def ReverseArray(arr):
    i = 0
    j = len(arr) - 1
    while(i < j):
        swap(arr, i, j)
        i += 1
        j -= 1
    return arr

print(ReverseArray(arr))
