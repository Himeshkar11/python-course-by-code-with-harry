# Write
# # a
# # function
# # that
# # prints
# # all
# # prime
# # numbers in a
# # given
# # range.

def isprime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:

            return False
    return True


n = int(input("enter the range of numbers"))
prime = []
for i in range(n+1):
    if isprime(i):
        prime.append(i)
    else:
        continue
print(prime)