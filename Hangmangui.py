
import tkinter as tk
import random

# Game Setup
words = ["python", "mahalakshmi", "subhasri", "prompt", "spark", "HDFS", "FAVOURITE"]
chosen_word = random.choice(words).lower()
word_display = ["_" for _ in chosen_word]
attempts = 15

# Main App Window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x300")
root.resizable(False, False)

# UI Elements
title_label = tk.Label(root, text="Welcome to Hangman", font=("Helvetica", 16))
title_label.pack(pady=10)

word_label = tk.Label(root, text=' '.join(word_display), font=("Helvetica", 18))
word_label.pack(pady=10)

attempts_label = tk.Label(root, text=f"Attempts left: {attempts}", font=("Helvetica", 14))
attempts_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 14), fg="green")
result_label.pack(pady=5)

guess_entry = tk.Entry(root, font=("Helvetica", 14))
guess_entry.pack(pady=10)

# Game Logic
def check_guess():
    global attempts
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if len(guess) != 1 or not guess.isalpha():
        result_label.config(text="Enter a single valid letter", fg="orange")
        return

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
        word_label.config(text=' '.join(word_display))
        result_label.config(text="Correct guess!", fg="green")
    else:
        attempts -= 1
        attempts_label.config(text=f"Attempts left: {attempts}")
        result_label.config(text=f"'{guess}' is not in the word.", fg="red")

    # Check win/loss condition
    if "_" not in word_display:
        result_label.config(text="You guessed it! You survived!", fg="blue")
        guess_button.config(state="disabled")
        guess_entry.config(state="disabled")
    elif attempts == 0:
        result_label.config(text=f"You ran out of attempts. Word was '{chosen_word}'.", fg="darkred")
        word_label.config(text=chosen_word)
        guess_button.config(state="disabled")
        guess_entry.config(state="disabled")

# Submit Button
guess_button = tk.Button(root, text="Guess", font=("Helvetica", 12), command=check_guess)
guess_button.pack(pady=10)

root.mainloop()
