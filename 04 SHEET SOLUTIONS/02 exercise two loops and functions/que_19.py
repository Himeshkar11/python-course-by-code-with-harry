def isprime(num):
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
    return True
print(isprime(29))
print(isprime(4))


