# Factor count: Given a number,
# count all its divisors using a loop.
n = int(input("Enter the number :"))
og = []
for i in range(n+1):
    if i == 0:
        continue
    elif n%i == 0:
        og.append(i)
print(len(og))

