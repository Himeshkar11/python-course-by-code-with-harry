# Program that asks for user input until valid integer is entered (with try-except).
while True :
    try:
        i = int(input("Please enter an integer here :"))
    except ValueError:
        print(ValueError)
