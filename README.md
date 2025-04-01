# Rock Paper Scissors Game with Machine Learning

This is a **Rock Paper Scissors** game built using Python and Tkinter, where the player competes against the computer. The game also incorporates a **Random Forest Classifier** for machine learning, which attempts to predict the player's next move based on the history of their previous choices.

## Features

- **Graphical User Interface (GUI)** built with Tkinter.
- **Machine Learning**: Uses Random Forest Classifier to predict the player's move.
- **Game Logic**: Classic Rock Paper Scissors with the option for the player to play against the computer.
- **Score Tracking**: Keeps track of the player's and computer's score over multiple rounds.
- **Game History**: Shows the outcome of each round and updates the score.
- **End Game**: After 5 rounds, the game ends and displays the winner.

## Requirements

To run the game, you need to have the following libraries installed:

- `tkinter`: For creating the GUI.
- `Pillow`: For handling image processing.
- `sklearn`: For implementing the Random Forest Classifier.
- `numpy`: For numerical operations.

You can install the required libraries by running:

```bash
pip install tkinter Pillow scikit-learn numpy
```

## How to Run:
1. Clone the repository to your local machine.
2. Install the necessary dependencies using the command above.
3. Place an image named image.png in the same directory as the script (or modify the code to use your own image).
4. Run the Python script:
```bash
python rock_paper_scissors_game.py
```
5. The game window will appear, allowing you to select Rock, Paper, or Scissors and compete against the computer. The game will continue for 5 rounds and display the final result.

## Game Flow
1. Round 1 to Round 5: You and the computer take turns to choose Rock, Paper, or Scissors.
2. The Random Forest Classifier will try to predict your next move based on previous rounds.
3. The winner of each round is determined and scores are updated.
4. After 5 rounds, the game ends and the winner is displayed.

## Example Gameplay
Player Choice: Rock
Computer Choice: Paper
Round Outcome: Computer wins!

