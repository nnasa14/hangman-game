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

class Hangman:
    def __init__(self):
        self.puzzle = []

    def correctGuess(self):
        pass

    def incorrectGuess(self):
        pass

    def test_char(self, char):
        for item in word.lower():
            if item == char:
                pass                #print it on the approppriate position

    def printGallows(self, counter):
        return counter
    
    def printPuzzle(self, puzzle):
        return puzzle

if __name__ == "__main__":
    word = "antiquated"        #get random string as a global variable
    
    while True:
        puzzle = 0
        counter = 0             #set counter
        Hangman.printGallows    #print gallows
        Hangman.printPuzzle     #print puzzle
        char = input("Guess a letter: ")
        Hangman.test_char       #test char
        if len(puzzle) == len(word):
            print("You won in {guesses} guesses!")
        if counter == 3000:
            print("You lost. The correct answer is: {word}")
