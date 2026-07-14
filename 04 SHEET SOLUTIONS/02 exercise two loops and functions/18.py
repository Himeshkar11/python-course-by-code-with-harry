# Write
# a
# function
# to
# check if a
# number is prime(using
# loops).

numb = int(input("Enter the number you want to test :"))
for i in range (2,int(numb**0.5)+1):
    if numb% i ==0:
        print("NOT prime")
        break
    else:
        print(f"yes {i} is prime")
