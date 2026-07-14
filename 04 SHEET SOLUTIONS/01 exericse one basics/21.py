#  21. Smart Calculator
#  Create a program that takes two numbers and an operator (+, -, *, /, %) and 
# performs the calculation.
# Handle division by zero and invalid operators with appropriate error messages.

a= int(input("Enter your first number here :"))
b= int(input("Enter your second number here :"))
print("Select one of the operators given below \n operator (+, -, *, /, )")
c= input("operators operator (+, -, *, /, )",)

if c == "+" :
    print("The sum of the two number is",a+b)
elif c =="-":
    print("The difference of the two number is",abs(a-b))
elif c=="*":
    print("The product of the two number is",a*b)
elif c == "/" :
    if b == 0:
        print("Err! division by zero is not possible")
    else:
        print("The divsion of the numbers is ",a/b)

    
    
