import tkinter as tk
import random

# Colors and Fonts
BG_COLOR = "#ffe6f0"
TEXT_COLOR = "#4d004d"
BTN_COLOR = "#ff99cc"
BTN_HOVER = "#ff66b3"
FONT = ("Press Start 2P", 10)  # Pixel-style font if installed

# Generate random number
secret_number = random.randint(1, 100)
attempts = 0

# Functions
def check_guess():
    global attempts, secret_number
    guess = entry.get()

    if not guess.isdigit():
        feedback.config(text=" Enter a valid number!")
        return

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        feedback.config(text=" Too low! Try again.")
    elif guess > secret_number:
        feedback.config(text=" Too high! Try again.")
    else:
        feedback.config(text=f" Correct! You guessed it in {attempts} tries!")

    if attempts == 5 and guess != secret_number:
        hint_range = (max(secret_number - 10, 1), min(secret_number + 10, 100))
        feedback.config(text=f"💡 Hint: It's between {hint_range[0]} and {hint_range[1]}")

def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    feedback.config(text="Guess a number between 1 and 100!")

# Create window
window = tk.Tk()
window.title("🎀 Number Guesser")
window.geometry("400x300")
window.configure(bg=BG_COLOR)

# Texts & Entry
label = tk.Label(window, text="Guess the number (1-100)", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR)
label.pack(pady=10)

entry = tk.Entry(window, font=FONT, width=10, justify="center", bg="#fff0f5")
entry.pack(pady=10)

guess_btn = tk.Button(window, text="Guess", font=FONT, bg=BTN_COLOR, fg=TEXT_COLOR, command=check_guess)
guess_btn.pack(pady=5)

reset_btn = tk.Button(window, text="Reset", font=FONT, bg=BTN_COLOR, fg=TEXT_COLOR, command=reset_game)
reset_btn.pack(pady=5)

feedback = tk.Label(window, text="Guess a number between 1 and 100!", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR)
feedback.pack(pady=20)

# Start app
window.mainloop()
