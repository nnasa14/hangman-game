import tkinter as tk
from tkinter import messagebox
from Hangman import Hangman
        

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
        char_guess_return = hangman_instance.test_char(char_guess)     
        print(puzzle_list)   
        attempts += 1             

        if char_guess_return == False:
            incorrect_attempts += 1
            print(f"Incorrect. You have {(guesses - incorrect_attempts)} attempts left.")   

        if incorrect_attempts == guesses:
            print(f"You lost. The correct answer is: {target_word}")
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
            print(f"You won in {attempts} guesses!")
            break
