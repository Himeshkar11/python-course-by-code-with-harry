n =18

# a guess the game program 
chance = 9
print("Welcome to the game \n you have 9 choices to guess the number \n after that game over")
while chance >0:
    user_input = int(input("Enter your number here "))
    if user_input == n :
        print(f"Hai number you chose{user_input} is correct  ")
        break
    elif user_input >n :
        print("The number you have enter is bigger then the number ")
        chance -= 1
        print(f"You have{chance} chances left.\n")

    else :

        print("The number you have entered is smaller than the number")
        chance -= 1
        print(f"You have{chance} chances left.\n")

    if chance == 0:
        print(f"Game over! The correct number was {n}")
    print("Thanks for playing the game !")