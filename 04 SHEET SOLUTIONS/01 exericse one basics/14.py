#  14. Leap Year Checker
#  Write a program that checks if a given year is a leap year.
# A year is a leap year if it's divisible by 4,
# except for years divisible by 100 imp
# (unless also divisible by 400 imp

a = int(input("Enter the Year here ",))

if (a%4==0 and a%100 !=0) or (a%400 ==0):
    print("Yes the year ", a , "is a leap year")
else :
    print("No the year",a,"is not a Leap year")
