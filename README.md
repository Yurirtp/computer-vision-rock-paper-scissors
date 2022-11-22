# Computer Vision RPS

## Milestone 1

This github repo was created

## Milestone 2

Images were taken of the rock, paper, scissors, and nothing options in teachable machine, and the model was downloaded.

Download the model from the "Tensorflow" tab in Teachable-Machine. The model should be named keras_model.h5 and the text file containing the labels should be named labels.txt.

The files you are downloading contain the structure and the parameters of a deep learning model. They are not files that can be run, and they do not contain anything readable if you look inside. Later, you will load them into your Python application in the next milestone.

Make sure you push the model and labels to your GitHub repository after committing.

## Milestone 3 

'''$ pip install library '''
    Collecting library
    Downloading Library-0.0.0.tar.gz (1.4 kB)
    Preparing metadata (setup.py) ... done
    Building wheels for collected packages: library
    Building wheel for library (setup.py) ... done
    Created wheel for library: filename=Library-0.0.0-py3-none-any.whl size=2055 sha256=4603da56f283cc04fc2891b08d1bb1a65a5d92c5e39afcf0b15b57fb52c9e82f
    Stored in directory: c:\users\yurir\appdata\local\pip\cache\wheels\52\cc\18\326d98d6504470bb5c6e275ddf218c212bdf0449d2944f34dc
    Successfully built library
    Installing collected packages: library
    Successfully installed library-0.0.0 '''

## Milestone 4 
Milestone 4 RPS game was created with the user typing in their choice. Using if/else statements. 


Create another file called manual_rps.py that will be used to play the game without the camera.

You will need to use the random module to pick a random option between rock, paper, and scissors and the input function to get the user's choice.

Create two functions: get_computer_choice and get_user_choice. The first function will randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice. The second function will ask the user for an input and return it

## Milestone 5 
Combination of milestone 3 and 4. This allows the user to show their choice to the camera and it returns the winner. There is an easy and hard mode where the computer does not randomly choose, and predicts based on the user choice. For MIlestone 5, get_prediction funtion was created by using the model as the main body, this model draws frames until the user quits or when the 5 second countdown finishes. It then returns a prediction of what the user has chosen. The model prints out a list of probabilities for each class. Then chooses the class with the highest probability. Whatever the probability corresponds to from the list is the users output. In milestone 5 includes combines everythong together to play game of rock paper scissors between the computer and the user thorugh a webcam. The player that wins 3 rounds is the winner.

![image](https://user-images.githubusercontent.com/116115861/203436413-e649823d-b189-4c07-a05b-4a06290bceca.png)
![image](https://user-images.githubusercontent.com/116115861/203436472-1c50cef8-c29c-4517-8c08-72f1eb2eebb3.png)
![image](https://user-images.githubusercontent.com/116115861/203436590-a2425085-9d65-4628-8f0c-3c66a1a56599.png)


Getting user input via Keras model
The function get_prediction() opens an openCV capture window and passes each capture frame to the input layer of the keras model. The captured frame is then displayed with a countdown timer in seconds and the current prediction of the model, for user feedback. When the countdown timer reaches zero, the move corresponding to the argmax of the softmax layer on that frame is returned as an output of the function.

Making the full game
The functions get_prediciton(), get_computer_choice() and get_winner() are wrapped as methods of a class, RPS. The init method of the class requires the keras model as an input, and assigns number of wins for each player as attributes.

The final game is then created using a function, play_game(), which creates an instance of RPS, and runs repeat instances of the game by calling its methods inside an iterating while loop, which terminates if either player reaches three wins.
