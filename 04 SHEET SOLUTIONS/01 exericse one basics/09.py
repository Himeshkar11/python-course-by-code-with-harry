# 9. Simple If Statement
#  Write a program that checks if a number is positive and prints "The number is positive" if true

a = int(input("Please enter your number here ",))

if a >0:
    print("Yes the number is positive")
elif a==0 :
    print("The number is neither positive nor negative")
else:
    print("The number is Negative")
