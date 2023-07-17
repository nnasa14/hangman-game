import json
import random

class Hangman:
    def __init__(self, word=None):
        if word is None:
            word = self.get_word()

        if word is not None:
            self.word = word
            self.puzzle = ["_" for _ in word]
        else:
            self.word = None
            self.puzzle = []

        #self.guessed_chars = []

    def get_word(self):
        with open("words.json", 'r') as file:
            word_list = json.load(file)

        word = random.choice(word_list)
        return word

    def __str__(self):
        return f"{target_word}"

    def test_char(self, char):
        for item in target_word.lower():
            if item == char:
                self.editPuzzle(char)     #print it on the approppriate position
                return self.puzzle

        incorrect_attempts =+ 1
        print(f"Incorrect. You have {incorrect_attempts} attempts left.")   #fix this so that the variable does not get reset each instance
        return 
    
    def editPuzzle(self, char):
        for index, item in enumerate(self.word):
            if char == item:
                self.puzzle[index] = char

    def guessWord(self, guess):
        if guess == target_word:
            print(f"Your guess, {guess}, was correct!")
        else:
            print(f"You guess, {guess}, was incorrect.")
        

if __name__ == "__main__":
    hangman_instance = Hangman()
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
