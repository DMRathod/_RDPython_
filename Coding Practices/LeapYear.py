
#   leap year is after every 4 years, divisible by 4.
#   Every Century years are not leap years means if it is divisible by 100.
#   we need to confirm if it is divisible by 400 or not. 

year = int(input("Enter The Year :"))
if(year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print(str(year) + "is Leap Year")
    else:
        print(str(year)+ "is Leap Year")
else:
    print(str(year) + " is NOT Leap Year")
