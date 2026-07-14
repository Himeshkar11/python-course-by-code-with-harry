# # operators in python
# arthimetic operators
# assignment operators
# comparision operator
# identity operator
# membership operator
# nitwise  operator
from operator import truediv

# Arthimetic operators
print("5+6 is", 5+6)
print("5-6 is", 5-6)
print("5*6 is", 5*6)
print("5/6 is", 5/6)
print("5//6 is", 5//6)  # this is like greaterst integer function
print("5%6 is", 5%6)    # this only ghive the remainder
print("5**6 is", 5**6)  # this is an exponential function

# assignment operator

print("Assignment operator")

x = 5
print(x)

x += 7
print(x)
x -= 7
print(x)

x *= 7
print(x)
# comparison operators
i = 5

print(i ==5)
print(i>=5)
print(i<=5)
print(i<5)
#logical operators

a = True
b =False

print( a and b )
print( a or b )
# just like truth table
#membership operator
listt = [a,b,c,d,e,f]

print(c in listt)
print(c not in listt)

#better not to mess with bitwise operator