import tkinter as tk
from tkinter import messagebox
import Hangman
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hangman")
    hangman_instance = Hangman()
    root.mainloop()

    target_word = hangman_instance.word

    difficulty = input("Please select your difficulty: (hard, normal, easy)")
    if difficulty == "hard":
        guesses = 3
    elif difficulty == "normal":
        guesses = 5
    elif difficulty == "easy":
        guesses = 7 
    else:
        print('Please run again and type "hard", "normal", or "easy".')

    incorrect_attempts = 0
    attempts = 0

    puzzle_list = hangman_instance.puzzle

    print(puzzle_list)

    while True:
        #if guesses == 0:
        #    break

        char_guess = str(input("Guess a letter: "))
        #print(f"Your guess was {char_guess}")
        hangman_instance.test_char(char_guess)     
        print(puzzle_list)   
        attempts += 1                    

        puzzle_str = ""
        for item in puzzle_list:                    #turn the list of "_" into a string
            puzzle_str += str(item)

        if puzzle_str == target_word:
            print(f"You won in {attempts} guesses!")
            break
        if incorrect_attempts == guesses:
            print(f"You lost. The correct answer is: {target_word}")
            break
