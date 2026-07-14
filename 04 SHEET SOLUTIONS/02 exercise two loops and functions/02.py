# #  Find all numbers between 100 and 1000 divisible
# # by the sum of their digits.
# n = int((input("Enter your number here")))
# if 100<int(n)<1000 :
#     print("So you selected",n)
# else :
#     print("Please enter a number in the given range")
# a = sum(int(i) for i in str(n) )
# if n%a == 0 :
#     print("yes divisible")
# else :
#     print("no")
 
for i in range(100,1000):
    a = sum(int(digit)for digit in str(i))
    if i%a == 0:
        print(i)