numbers = [1, 1, 3, 4, 5, 5, 4, 3, 8]

def FindUnique(numbers):
    result = 0
    for number in numbers:
        result ^=  number
    return result

print(FindUnique(numbers)) # 8
