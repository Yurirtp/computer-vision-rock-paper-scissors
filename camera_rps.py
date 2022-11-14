# %%
import random
import cv2
from keras.models import load_model
import numpy as np
import time

def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    print("Get ready")
    start = time.time()
    end = start + 10
    while time.time() <= end: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        max_value_index = np.argmax(prediction[0], axis=0)
        choice = {0: "Nothing",  1: "rock", 2: "paper", 3: "scissors"}
        user_choice =  choice[max_value_index]
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        elif time.time() == end: 
            return user_choice
            # After the loop release the cap object 
    cap.release()
    cv2.destroyAllWindows()
    return str(user_choice)

   
    

    # Destroy all the windows

  
def get_computer_choice():
    comp_list = ['rock','paper','scissors']
    computer_choice = random.choice(comp_list)
    return computer_choice


def get_winner(computer_choice, user_choice):
    print(f"The computer picked {computer_choice}, you picked {user_choice}")
    if user_choice == computer_choice:
            result = ("It is a tie!")
    elif (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock"):
        result ="You won!"
    else: result = "You lost" 
    print(result)   

def get_logic(outcome):
    computer_choice = get_computer_choice()
    user_choice = get_prediction()
    outcome = get_winner(computer_choice, user_choice)
    computer_wins = 0 
    user_wins = 0 
    while not (computer_wins == 3 or user_wins ==3):
        if outcome == "You lost":
            computer_wins+=1
        elif outcome == "You won!":
            user_wins+=1
        else: 
            pass    

    if computer_wins == 3 and computer_wins > user_wins:
        print("Computer is the winner!")
    elif user_wins == 3 and user_wins > computer_wins:
        print("Congratulations the User Wins!")
    else:
        pass
    print(f"Final scores are: Computer {computer_wins} VS. You {user_wins}")
    cv2.destroyAllWindows()

def play():
    outcome = get_winner()
    logic = get_logic(outcome)
    logic

play()

# %%
