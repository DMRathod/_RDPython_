
number = 6
def Factorial(number):
    if(number == 1):
        return 1
    return number * Factorial(number - 1)

print(Factorial(number))