from tkinter import *
import random

# Function to handle the number guessing logic
def start_game():
    global number_of_guesses, random_number
    random_number = random.randint(1, 20)  # Random number between 1 and 20
    number_of_guesses = 0
    result_label.config(text="Guess a number between 1 and 20.")
    guess_button.config(state=NORMAL)
    guess_entry.delete(0, END)
    guesses_left_label.config(text=f"Guesses left: 9")
    game_over_label.place_forget()
    result_label.place(x=70, y=150)  # Ensure result label appears again after game over

# Function to check the player's guess
def check_guess(event=None):  # Allow event to trigger on pressing Enter
    global number_of_guesses, random_number
    try:
        guess = int(guess_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    number_of_guesses += 1

    if guess < random_number:
        result_label.config(text="Too low! Try a higher number.")
    elif guess > random_number:
        result_label.config(text="Too high! Try a lower number.")
    else:
        result_label.config(text=f"Congratulations! You've won in {number_of_guesses} guesses.")
        guess_button.config(state=DISABLED)
        result_label.place(x=70, y=150)  # Display result message after win
        game_over_label.place_forget()  # Hide "Game Over" message after win
        root.after(5000, start_game)  # Restart game after 5 seconds
        return

    # Update the remaining guesses count
    guesses_left_label.config(text=f"Guesses left: {9 - number_of_guesses}")

    if number_of_guesses >= 9:
        result_label.config(text=f"Game Over! The number was {random_number}.")
        guess_button.config(state=DISABLED)
        game_over_label.place(x=120, y=200)  # Show the "Game Over" label
        root.after(5000, start_game)  # Restart game after 5 seconds

    # Clear the input field after checking the guess
    guess_entry.delete(0, END) 
    
# Create the main window
root = Tk()
root.title("Number Guessing Game")
root.geometry("500x400")
root.config(bg="#1a1a2e")  # Dark background color

# Title Label
title_label = Label(root, text="Number Guessing Game", font=("Helvetica", 30, "bold"), fg="white", bg="#1a1a2e")
title_label.pack(pady=20)

# Instructions Label
instructions_label = Label(root, text="Guess the number between 1 and 20.", font=("Helvetica", 14), fg="white", bg="#1a1a2e")
instructions_label.pack(pady=10)

# Entry to input guesses
guess_entry = Entry(root, font=("Helvetica", 20), bd=2, relief=SOLID)
guess_entry.pack(pady=40)

# Result Label to display feedback
result_label = Label(root, text="Enter a number and press Guess.", font=("Helvetica", 14), fg="white", bg="#1a1a2e")
result_label.pack(pady=10)

# Label to show the remaining number of guesses
guesses_left_label = Label(root, text="Guesses left: 9", font=("Helvetica", 14), fg="white", bg="#1a1a2e")
guesses_left_label.pack(pady=10)

# Button to check the guess
guess_button = Button(root, text="Guess", font=("Helvetica", 14), bg="#e94560", fg="white", command=check_guess)
guess_button.pack(pady=20)

# Button to start a new game
start_button = Button(root, text="Start New Game", font=("Helvetica", 14), bg="#4caf50", fg="white", command=start_game)
start_button.pack(pady=10)

# Game Over Label (hidden initially)
game_over_label = Label(root, text="Game Over!", font=("Helvetica", 24, "bold"), fg="red", bg="#1a1a2e")

# Start the game when the window is loaded
start_game()

# Bind the Enter key to trigger the check_guess function
root.bind('<Return>', check_guess)

# Run the main loop
root.mainloop()
