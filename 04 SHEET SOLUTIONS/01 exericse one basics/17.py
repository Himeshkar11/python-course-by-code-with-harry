#   17. Triangle Type
#  Write a program that takes three sides of a triangle and determines
# if it's "equilateral" (all sides equal), 
# "isosceles" (two sides equal), 
# or "scalene" (no sides equal)

a = int(input("Enter the length of first side of the triangle here ",))
b = int(input("Enter the length of second side of the triangle here ",))
c = int(input("Enter the length of third side of the triangle here ",))

if a==b==c:
    print("the triangle is an equilateral triangle")
elif (a==b!=c) or (a!=b==c) or (a==c!=b):
    print("The given triangle is an isosceles triangle" )
else :
    print("the triangle which you entered is a scalene triangle")