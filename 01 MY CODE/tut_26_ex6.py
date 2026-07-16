# a custom stone paper scissors against the computer have ten chances after that majority is declared win


def computercall():
    import random
    choices =["rock","paper","scissors"]
    computer_choice = random.choice(choices)
    return computer_choice
#  24. Rock, Paper, Scissors Logic
#  Create the logic for a Rock, Paper, Scissors game.
# Take two inputs (player choices) and determine the winner
# or if it's a tie, with detailed explanations

print("Welcome to the game of \"rock paper scissors\"")
i = 10
computer_win = 0
user_win = 0
while i>0:

    i = i-1
    user_choice=input("Enter any one choice ",)
    computer_choice= computercall()



    if computer_choice == user_choice:
        print(f"It is a draw \n ")
        user_win += 0
        computer_win += 0
    elif computer_choice == "rock" and user_choice=="paper":
        print(f"computer choose : {computer_choice}")
        print(f"user  choose : {user_choice}")
        print("user wins")
        user_win += 1
    elif computer_choice == "rock" and user_choice=="scissors":
        print(f"computer choose{computer_choice}")
        print(f"user  choose{user_choice}")
        print(f"computer wins ")
        computer_win += 1
    elif computer_choice == "paper" and user_choice == "rock":
        print(f"computer choose{computer_choice}")
        print(f"user  choose{user_choice}")
        print(f"computer wins ")
        computer_win += 1
    elif computer_choice == "paper" and user_choice == "scissors":
        print(f"computer choose{computer_choice}")
        print(f"user  choose{user_choice}")
        print(f"user  wins ")
        user_win += 1
    elif computer_choice == "scissors" and user_choice == "rock":
        print(f"computer choose{computer_choice}")
        print(f"user  choose{user_choice}")
        print(f"user  wins ")
        user_win += 1
    elif computer_choice=="scissors" and user_choice == "paper":
        print(f"computer choose{computer_choice}")
        print(f"user  choose{user_choice}")
        print(f"computer wins ")
        computer_win += 1
    else :
        print("ERR! please run again")
    print(f"points are \n computer : {computer_win} \n user : {user_win} \n ")
    print("NO OF GAMES LEFT ",i)

if user_win > computer_win:
    print("You won")
elif user_win == computer_win:
    print("it is a draw")
else:
    print("You lost")
