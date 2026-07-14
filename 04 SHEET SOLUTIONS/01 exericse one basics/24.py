#  24. Rock, Paper, Scissors Logic
#  Create the logic for a Rock, Paper, Scissors game. 
# Take two inputs (player choices) and determine the winner 
# or if it's a tie, with detailed explanations

print("Welcome to the game of \"rock paper scissors\"")
user1_choice=input("Enter any one choice ",)
user2_choice=input("Enter any one choice ",)

if user1_choice == user2_choice:
    print("It is a draw")
elif user1_choice == "rock" and user2_choice=="paper":
    print("user2 wins")
elif user1_choice == "rock" and user2_choice=="scissors":
    print("user 2 wins")
elif user1_choice == "paper" and user2_choice == "rock":
    print("User 1 wins")
elif user1_choice == "paper" and user2_choice == "scissors":
    print("user 2 wins")
elif user1_choice == "scissors" and user2_choice == "rock":
    print("user 2 wins")
elif user1_choice=="scissors" and user2_choice == "paper":
    print("user 1 wins")
else:
    print("ERR! please run again")