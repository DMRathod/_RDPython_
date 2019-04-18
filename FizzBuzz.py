#this is my fizzBuzz program
def FizzBuzz(value_1,value_2,range_start,range_end):
    for i in range(range_start,range_end):
        if(i % value_1 == 0 and i % value_2 == 0):
            print("Fizz Buzz",i)
        elif(i % value_1 == 0):
            print("Fizz",i)
        elif(i % value_2 == 0):
            print("Buzz",i)
        else:
            print(i)