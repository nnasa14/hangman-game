#generate word
#print the gallows and empty letter spaces
#ask for user input
#respond to incorrect by adding the hangman onto gallows
#respond to correct input by adding letter into the correct position(s)
#repeat until either the hangman is completed or the word is solved

#randomly select a word from the json file
#print the gallows and amount of chars in the word (spaces will stay as spaces)
#ask for user input
#if input is in word, replace _ with char when appropriate
#else, print a limb on the gallows (add a counter to keep track of this)
#when counter reaches its end point, print you lose and reveal the word
#when len of puzzle == len word, print you won
import random

class Hangman:
    def __init__(self):
        self.puzzle = []

    def __str__(self):
        return f"{self.puzzle}"

    def random_word(self):
        with open("words.json", 'r') as file:
            word_list = "words.json"(file)

        random_word = random.choice(word_list)
        return random_word

    def test_char(self, char):
        for item in word.lower():
            if item == char:
                Hangman().printPuzzle(char)     #print it on the approppriate position
            else:
                attempts =+ 1
                return f"Incorrect. You have {attempts} attempts left."
    
    def printPuzzle(self, char):
        for item in word:
            if char == " ":
                print(item)
            if char == item:
                print(char)
            else:
                print("_")
        

if __name__ == "__main__":
    hangman = Hangman()
    
    word = hangman.random_word        #get random string as a global variable

    difficulty = input("Please select your difficulty: (hard, normal, easy)")
    if difficulty == "hard":
        guesses = 3
    elif difficulty == "normal":
        guesses = 5
    elif difficulty == "easy":
        guesses = 7 
    else:
        print('Please run again and type "hard", "normal", or "easy".')


    while True:
        if guesses == 0:
            break
        puzzle = 0
        attempts = 0
        char = input("Guess a letter: ")
        print(Hangman.test_char)       #test char
        if len(puzzle) == len(word):
            print("You won in {guesses} guesses!")
        if attempts == guesses:
            print("You lost. The correct answer is: {word}")
