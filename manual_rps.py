#%%
import random 


def get_computer_choice():
    comp_choice = ['rock','paper', 'scissors']
    x = random.choice(comp_choice)
    return x


def get_user_choice():
    user_choice = input("Play")
    print(user_choice)




get_user_choice()
get_computer_choice()

