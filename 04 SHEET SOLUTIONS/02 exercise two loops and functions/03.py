#  Print all prime palindrome numbers 
# between two given numbers.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
for n in range(a,b+1):
    
    if str(n) == str(n)[::-1]:

        if n <2:
            continue
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break
        else:
            print(n)