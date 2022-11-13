#%%
import random 

def get_computer_choice():
    comp_list = ['rock','paper','scissors']
    computer_choice = random.choice(comp_list)
    return computer_choice

def get_user_choice():
    user_choice = input("Play")
    return user_choice


def get_winner(computer_choice, user_choice):
    print(f"The computer picked {computer_choice}, you picked {user_choice}")
    if user_choice == computer_choice:
            result = ("It is a tie!")
    elif (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock"):
        result =("You won!")
    else: result = "You lost" 
    print(result)    

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)

play()
