# 13. Grade Calculator
#  Write a program that takes a numerical score 0100) 
# and prints the letter grade:
# A 90-100,
# B 80-89,
# C 70-79, 
# D 60-69, 
# F (below 60

a = int(input("Please enter the numbers form 0 to 100 ",))

if 0<=a<=100:
    print("Are you sure that you choose",a)
    
    if  90<=a<=100:
        print("Then your grade will be A")

    elif 80<=a<=89:
         print("Then your grade will be B")
    elif 70<=a<=79:
        print("Then your grade will be C")
    elif 60<=a<=69:
        print("Then your grade will be D")
    else :
        print("You have Failed")
    
else:
    print("Please enter the number again by pressing run again ")




