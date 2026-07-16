#sometimes an error will come into our program and we dont want t to shut down so now we use try except to bypass the err
from logging import exception

try:
    a = int(input("enter your number "))
    print(f"multiplication table is {a} is ")
    for i in range(1,11):
        print(f"{i} x {a} is {a*i}")
except Exception as e:
    print(e)


print("YOSUKE")

