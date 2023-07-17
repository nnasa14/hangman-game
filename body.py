import random

class Hangman:
    def __init__(self):
        with open("words.json", 'r') as file:
            word_list = "words.json"(file)

        word = random.choice(word_list)
        self.word = word

    def __str__(self):
        return f"{self.word}"

    def random_word(self):
        with open("words.json", 'r') as file:
            word_list = "words.json"(file)

        random_word = random.choice(word_list)
        return random_word

    def test_char(self, char):
        for item in self.word.lower():
            if item == char:
                Hangman().printPuzzle(char)     #print it on the approppriate position
            else:
                incorrect_attempts =+ 1
                return f"Incorrect. You have {incorrect_attempts} attempts left."
    
    def printPuzzle(self, char):                #need to fix this to rememeber previous inputs
        for item in self.word:
            if char == " ":
                print(item)
            if char == item:
                print(char)
            else:
                print("_")
        

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
    puzzle = ""

    while True:
        if guesses == 0:
            break

        char = input("Guess a letter: ")
        print(Hangman.test_char)                            #test char

        if len(puzzle) == len(target_word):
            print("You won in {guesses} guesses!")
        if incorrect_attempts == guesses:
            print("You lost. The correct answer is: {word}")
