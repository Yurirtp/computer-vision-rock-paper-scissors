# %%
import random
import cv2
from keras.models import load_model
import numpy as np
import time


class rock_paper_scissors:
    def __init__(self, comp_list):
        self.comp_list = comp_list
        self.computer_wins = 0
        self.user_wins = 0

    def get_prediction(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        print("Get ready!")
        print("Image will be captured in 5 seconds.")
        start = time.time()
        end = start + 5
        while time.time() <= end: 
            _, frame = cap.read()
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

    def get_computer_choice(self):
        computer_choice = random.choice(self.comp_list)
        return computer_choice


    def get_winner(self, computer_choice, user_choice):
        print(f"The computer picked {computer_choice}, you picked {user_choice}")
        if (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock"):
            result = "You won!"
            self.user_wins = self.user_wins + 1 
            pass
        elif (computer_choice == "paper" and user_choice == "rock") or (computer_choice == "scissors" and user_choice == "paper") or (computer_choice == "rock" and user_choice == "scissors"):
            result = "You lost"
            self.computer_wins = self.computer_wins + 1
            pass
        else: result = ("It is a tie!")
        pass
        print(result)
        

def play(comp_list = ['rock','paper','scissors']):
    xro = rock_paper_scissors(comp_list)
    wins = 0
    winz = 0
    while True:
            computer_choice = xro.get_computer_choice()
            user_choice = xro.get_prediction()
            xro.get_winner(computer_choice, user_choice)
            wins = xro.computer_wins
            winz = xro.user_wins
            if wins == 3 and wins > winz:
                print("Computer is the winner!")
                break
            elif winz == 3 and winz > wins:
                print("Congratulations the User Wins!")
                break
    print(f"Final scores are: Computer {wins} VS. You {winz}")


play()
       
        

        





