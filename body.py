"""import tkinter as tk
from tkinter import messagebox
from Hangman import Hangman
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hangman")
    hangman_instance = Hangman()
    root.mainloop()

    target_word = hangman_instance.word

    guesses = 6
    incorrect_attempts = 0
    attempts = 0

    puzzle_list = hangman_instance.puzzle

    messagebox.showinfo(puzzle_list)

    while True:
        char_guess = str(input("Guess a letter: "))
        char_guess_return = hangman_instance.test_char(char_guess)     
        messagebox.showinfo(puzzle_list)   
        attempts += 1             

        if incorrect_attempts == guesses:
            messagebox.showinfo(f"You lost. The correct answer is: {target_word}")
            break    

        puzzle_str = ""
        for item in puzzle_list:                        #turn the list of "_" into a string
            puzzle_str += str(item)

        guess_word_return = ""                          #guess a word
        guess_word = input("Guess the word? (y/n) ")
        if guess_word == "y":
            input_guess = input("What is your guess? ")
            guess_word_return = hangman_instance.guessWord(input_guess)

        if puzzle_str == target_word or guess_word_return == True:  #determine if completed inputs or guessed word is correct
            messagebox.showinfo(f"You won in {attempts} guesses!")
            break
"""