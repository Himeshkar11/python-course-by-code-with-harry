#  15. Number Comparison
#  Write a program that takes three numbers 
# and prints which one is the largest
a = int(input("ENTER YOUR FIRST NUMBER"))
b = int(input("ENTER YOUR SECOND NUMBER"))
c = int(input("ENTER YOUR THIRD NUMBER"))

list_1 = [a,b,c]

d=max(list_1)

print(d)

# another way 
if a>=b and b>=c :
    print("The largest number is" ,a)
elif b>=a and a>=c:
    print("the greatest number is ",b)
    print("the greatest number is ",b)
else :
    print("the greatest number is ",c)
    
    
