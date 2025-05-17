# Hangman-python-project
This is a Graphical User Interface (GUI) version of the classic Hangman game, built using Python and Tkinter.
Guess the hidden word, one letter at a time. You have a total of 15 attempts to reveal all the letters in the word. If you guess the word before you run out of attempts, you win. Otherwise, you lose.

This is a Graphical User Interface (GUI) version of the classic Hangman game, built using Python and Tkinter.

 Objective:
Guess the hidden word, one letter at a time. You have a total of 15 attempts to reveal all the letters in the word. If you guess the word before you run out of attempts, you win. Otherwise, you lose.

Features:
Random Word Selection: The game randomly selects a word from a predefined list each time it starts.

Masked Word Display: The word is shown as underscores (_) representing unguessed letters.

Interactive Input: Players type a single letter into a text entry field and click Guess to submit.

Real-Time Feedback: After each guess:

If correct, the corresponding blanks in the word are filled in.

If incorrect, the number of remaining attempts decreases.

Attempt Tracking: Shows how many guesses are left.

End-of-Game Alerts:

 If you win: "You guessed it! You survived!"

If you lose: "You ran out of attempts. Word was '...'."

Input Validation: Prevents non-letter or multi-character input.
 Technologies Used:
Language: Python

GUI Library: Tkinter

