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

        self.incorrect_attempts = 0
        #self.guessed_chars = []

    def get_word(self):
        with open("words.json", 'r') as file:
            word_list = json.load(file)

        word = random.choice(word_list)
        return word

    def __str__(self):
        return f"{self.word}"

    def test_char(self, char):
        for item in self.word.lower():
            if item == char:
                self.editPuzzle(char)     #print it on the approppriate position
                return self.puzzle

        self.incorrect_attempts =+ 1
        print(f"Incorrect. You have {self.incorrect_attempts} attempts left.")   #fix this so that the variable does not get reset each instance
        return 
    
    def editPuzzle(self, char):
        for index, item in enumerate(self.word):
            if char == item:
                self.puzzle[index] = char

    def guessWord(self, guess):
        if guess == self.word:
            return True
        else:
            self.incorrect_attempts =+ 1
            print(f"You guess, {guess}, was incorrect.")
            return