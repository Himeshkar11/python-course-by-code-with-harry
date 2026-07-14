#exercise 2 i n python we have to  make a faulty calculator which
#45*3 = 555 ,56+9 = 77,56/6 = 4 which will give these values if inout is like this

#lets try

a = int(input("Enter your number one here ",))
b = int(input("Enter your number two here ",))

operations  = ["+","-","*","/"]

op = input("Enter your operation ")
if a == 45 and b == 3 and op == "*":
    print("455")
elif a == 56 and b == 9 and op == "+":
    print("77")
elif a == 56 and b == 6 and op == "/":
    print("4")
else: 
    if op == "+" :
        print(a+b)
    if op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/" :
        print(a/b)



