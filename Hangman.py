import json
import random

class Hangman:
    """
    A class of functions that fulfil the rules of a Hangman game

    Attributes:
        word(str): Randomly generated word
        puzzle(list): List of "_"s that represent each character of self.word

    Methods:
        get_word: Randomly generates a word as self.word
        test_char(char): Determines if inputted character is within self.word
        editPuzzle(char): Places a correctly guessed character in thier appriopriate position of self.puzzle
        guessWord(guess): Validates if a guessed word is self.word
    """
    def __init__(self, word=None):
        if word is None:
            word = self.get_word()

        if word is not None:
            self.word = word
            self.puzzle = ["_" for _ in word]
        else:
            self.word = None
            self.puzzle = []

    def __str__(self):
        return f"{self.word}"

    def get_word(self):
        """
        Function to randomly generate a word.

        Returns:
            A randomly word from a list of words in words.json
        """
        with open("words.json", 'r') as file:
            word_list = json.load(file)

        word = random.choice(word_list)
        return word


    def test_char(self, char):
        """
        Function that checks if a character is within self.word

        Parameters:
            char(str): An inputed character

        Returns:
            if char is in self.word, return the character in its correct position in self.puzzle
            if not, return a False value
        """
        for item in self.word.lower():
            if item == char:
                self.editPuzzle(char)     
                return self.puzzle
    
        return False
    
    def editPuzzle(self, char):
        """
        Function that adds a character to its corresponding position in self.word in self.puzzle

        Parameters:
            char(str): Character that was validated in test_char
        """
        for index, item in enumerate(self.word):
            if char == item:
                self.puzzle[index] = char

    def guessWord(self, guess):
        """
        Function that validates a guessed word to see if it matches self.word

        Parameters:
            guess(str): Guessed word

        Return:
            if guess is the same as self.word, return True
            if not, return None
        """
        if guess == self.word:
            return True
        else:
            self.incorrect_attempts =+ 1
            print(f"Your guess, {guess}, was incorrect.")
            return