

import tkinter as tk
from PIL import Image, ImageTk
import random
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Define class labels for moves
moves = {
    0: 'Rock',
    1: 'Paper',
    2: 'Scissors'
}

# Create the main GUI window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("1000x900")  # Set the initial size of the window
window.configure(bg='#333333')  # Set background color to dark gray

# Initialize game variables
round_number = 1
player_score = 0
computer_score = 0

# Previous moves list for machine learning
previous_moves = []

# Create a Random Forest Classifier for machine learning
clf = RandomForestClassifier(n_estimators=100, random_state=42)

def play_game(player_move):
    global round_number, player_score, computer_score, previous_moves, clf
    player_move = int(player_move)
    computer_move = random.randint(0, 2)  # Generate random computer move (0-Rock, 1-Paper, 2-Scissors)

    # Add player's move to previous moves list
    previous_moves.append(player_move)

    # Train the machine learning model with previous moves if there are enough samples
    if len(previous_moves) >= 2:
        X_train = previous_moves[:-1]
        y_train = previous_moves[1:]
        X_train = np.array(X_train).reshape(-1, 1)  # Reshape X_train to be a 2D array
        clf.fit(X_train, y_train)  # Fit the model with the reshaped data

    # Determine the winner
    if player_move == computer_move:
        outcome = 'Tie'
    elif (player_move + 1) % 3 == computer_move:
        outcome = 'Computer'
        computer_score += 1
    else:
        outcome = 'Player'
        player_score += 1

    # Update game log and scores
    log_label.config(state=tk.NORMAL)
    log_label.insert(tk.END, f"Round {round_number}: Player chose {moves[player_move]}, Computer chose {moves[computer_move]}. Winner: {outcome}\n")
    log_label.config(state=tk.DISABLED)

    round_number += 1
    round_label.config(text=f"Round {round_number}", fg='#333333', font=('Arial', 16, 'bold'))
    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}", fg='#333333', font=('Arial', 14, 'bold'))

    # Check if 5 rounds are completed
    if round_number > 5:
        end_game()

# Function to end the game after 5 rounds
def end_game():
    global player_score, computer_score, previous_moves
    winner = 'Player' if player_score > computer_score else ('Computer' if player_score < computer_score else 'Tie')
    result_text = f"{winner} wins with a score of {player_score}-{computer_score}!"

    # Create a new window for displaying the result
    result_window = tk.Toplevel()
    result_window.title("Game Result")
    result_window.geometry("600x400")  # Set the size of the result window
    result_window.configure(bg='#333333')  # Set background color to dark gray

    # Create a label to display the result
    result_label = tk.Label(result_window, text=result_text, font=('Arial', 24, 'bold'), fg='#e74c3c', bg='#333333')
    result_label.pack(padx=20, pady=50)

    # Function to restart the game
    def restart_game():
        global round_number, player_score, computer_score, previous_moves, clf
        round_number = 1
        player_score = 0
        computer_score = 0
        previous_moves = []
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        round_label.config(text=f"Round {round_number}", fg='#333333', font=('Arial', 16, 'bold'))
        score_label.config(text=f"Player: {player_score}  Computer: {computer_score}", fg='#333333', font=('Arial', 14, 'bold'))
        log_label.config(state=tk.NORMAL)
        log_label.delete("1.0", tk.END)
        log_label.config(state=tk.DISABLED)
        result_window.destroy()

    # Create a button to restart the game
    restart_button = tk.Button(result_window, text="Restart", command=restart_game, font=('Arial', 16), bg='#3498db', fg='#333333')
    restart_button.pack(pady=20)

    result_window.mainloop()

# Create labels and buttons with customized styles
instruction_label = tk.Label(window, text="Select your move:", font=('Arial', 20, 'bold'), padx=10, pady=20, bg='#333333', fg='#e74c3c')
instruction_label.pack()

button_frame = tk.Frame(window, bg='#333333')
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game(0), width=10, height=2, font=('Arial', 16), bg='#e74c3c', fg='#333333')
rock_button.pack(side=tk.LEFT, padx=10, pady=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game(1), width=10, height=2, font=('Arial', 16), bg='#e74c3c', fg='#333333')
paper_button.pack(side=tk.LEFT, padx=10, pady=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game(2), width=10, height=2, font=('Arial', 16), bg='#e74c3c', fg='#333333')
scissors_button.pack(side=tk.LEFT, padx=10, pady=10)

log_label = tk.Text(window, width=60, height=10, font=('Arial', 12), state=tk.DISABLED)
log_label.pack(pady=20)

round_label = tk.Label(window, text=f"Round {round_number}", font=('Arial', 16, 'bold'), fg='#333333', bg='#e74c3c')
round_label.pack()

score_label = tk.Label(window, text=f"Player: {player_score}  Computer: {computer_score}", font=('Arial', 14, 'bold'), fg='#333333', bg='#333333')
score_label.pack()

result_label = tk.Label(window, text="", font=('Arial', 20, 'bold'), fg='#e74c3c', bg='#333333')
result_label.pack(pady=20)

# Load and display an image
image_path = "image.png"
image = Image.open(image_path)
image = image.resize((300, 300), Image.LANCZOS)  # Use Image.LANCZOS for antialiasing
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(window, image=photo, bg='#333333')
image_label.pack(pady=20)

window.mainloop()