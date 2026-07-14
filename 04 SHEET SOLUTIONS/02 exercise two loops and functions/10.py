#  Ask the user to input a number and 
# use try-except to handle if input is not a number.
try :
    a = int(input("Enter a number: "))
except Exception as e:
    print(e,"Please enter a number")

