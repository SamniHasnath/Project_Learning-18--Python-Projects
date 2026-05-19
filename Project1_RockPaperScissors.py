#PYTHON PROJECT ROCK PAPER SCISSORS
#0 for Rock
#1 for Paper
#3 for Scissors
import random
print("🎮 Welcome to Rock, Paper, Scissors!")
user_choice=int(input("Enter your choice : 0 for Rock, 1 for Paper, 2 for Scissors :\n"))
if user_choice>=3 or user_choice<0:
    print("You entered invalid number, You lose")
else:
    computer_choice=random.randint(0,2)
    print("Computer Chose:")
    print(computer_choice)
    if computer_choice==user_choice:
        print("Game is a draw.")
    elif computer_choice==0 and user_choice==2:
        print("User loses.")
    elif user_choice==0 and computer_choice==2:
        print("User wins.")
    elif computer_choice>user_choice:
        print("User loses.")
    elif user_choice>computer_choice:
        print("User wins.")
