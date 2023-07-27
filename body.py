import tkinter as tk
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

    print(puzzle_list)

    while True:
        char_guess = str(input("Guess a letter: "))
        char_guess_return = hangman_instance.test_char(char_guess)     
        print(puzzle_list)   
        attempts += 1             

        hangman_instance.draw_gallows

        if char_guess_return == False:
            incorrect_attempts += 1
            print(f"Incorrect. You have {(guesses - incorrect_attempts)} attempts left.")
            if incorrect_attempts == 1:
                hangman_instance.draw_head
            elif incorrect_attempts == 2:
                hangman_instance.draw_left_arm   
            elif incorrect_attempts == 3:
                hangman_instance.draw_right_arm   
            elif incorrect_attempts == 4:
                hangman_instance.draw_left_leg   
            elif incorrect_attempts == 5:
                hangman_instance.draw_right_leg   
            elif incorrect_attempts == 6:
                hangman_instance.draw_ending   

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
