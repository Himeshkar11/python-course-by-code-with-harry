# Write a program that asks the user for two numbers and prints their division. Handle division
#  by zero and invalid inputs with try-except.

a = int(input("Please enter your first number"))
b = int(input("Please enter your second number"))

try :
     c = a/b
     print(c)
except Exception as e:
    print(e,": Is not allowed here \n try again")
