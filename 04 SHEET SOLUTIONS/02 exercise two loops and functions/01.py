# #Generate a diamond pattern of *
#  given an odd integer n.
n = int(input("Enter an odd integer: "))
for stars in range(1,n+1,2):
    print(("*"*stars).center(n))
    
for stars in range(n-2,0,-2):
    print(("*"*stars).center(n))
