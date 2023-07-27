import tkinter as tk
from tkinter import messagebox
import json
import random

class Hangman:
    """
    A class of functions that fulfil the rules of a Hangman game

    Methods:
        new_game: Randomly generates a word as self.word
        test_char(char): Determines if inputted character is within self.word
        editPuzzle(char): Places a correctly guessed character in thier appriopriate position of self.puzzle
        guessWord(guess): Validates if a guessed word is self.word
    """
    def __init__(self, master):
        self.master = master
        with open("words.json", 'r') as file:
            self.word_list = json.load(file)
        self.word = ""
        self.guesses = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()

        self.restart_button = tk.Button(master, text="New Game",command=self.start_game)
        self.start_game()

    """def __str__(self):
        return f'{self.word}'"""
    
    def start_game(self):
        self.word = random.choice(self.word_list)
        self.guesses = []
        self.attempts_left = self.max_attempts
        self.draw_gallows()

        self.word_display = tk.StringVar()
        self.word_display.set(" ".join("_" if char.isalpha() else char for char in self.word))
        self.word_label = tk.Label(self.master, textvariable=self.word_display, font=('Helvetica', 16))
        self.word_label.pack()

        self.guess_entry = tk.Entry(self.master, font=('Helvetica', 16))
        self.guess_entry.pack()
        self.guess_entry.focus()

        self.submit_button = tk.Button(self.master, text = "Guess", command=self.check_guess)
        self.submit_button.pack()

    def draw_gallows(self):
        self.canvas.delete("hangman")
        x0, y0 = 20, 280
        x1, y1 = 120, 280

        if self.attempts_left < self.max_attempts:
            self.canvas.create_line(x0, y0, x1, y1, tags="hangman")
            self.canvas.create_line(x0 + 50, y0, x1 + 50, y1, tags="hangman")
            self.canvas.create_line(x0, y0, x0 + 50, y0, tags="hangman")
            self.canvas.create_line(x0, y0 - 200, x0, y0, tags="hangman")
            self.canvas.create_line(x1, y0 - 200, x1, y0, tags="hangman")

        if self.attempts_left < self.max_attempts - 1:
            self.canvas.create_oval(x0 + 25, y0 - 200, x1 - 25, y0 - 150, tags="hangman")

        if self.attempts_left < self.max_attempts - 2:
            self.canvas.create_line(x0 + 50, y0 - 150, x0 + 50, y0 - 100, tags="hangman")

        if self.attempts_left < self.max_attempts - 3:
            self.canvas.create_line(x0 + 50, y0 - 100, x0 + 25, y0 - 75, tags="hangman")

        if self.attempts_left < self.max_attempts - 4:
            self.canvas.create_line(x0 + 50, y0 - 100, x0 + 75, y0 - 75, tags="hangman")

        if self.attempts_left < self.max_attempts - 5:
            self.canvas.create_line(x0 + 50, y0 - 200, x0 + 25, y0 - 225, tags="hangman")

        if self.attempts_left < self.max_attempts - 6:
            self.canvas.create_line(x0 + 50, y0 - 200, x0 + 75, y0 - 225, tags="hangman")

    def restart(self):
        self.word_label.pack_forget()
        self.guess_entry.pack_forget()
        self.submit_button.pack_forget()
        self.restart_button.pack_forget()
        self.canvas.delete("hangman")
        self.start_game()

    #def test_char(self, char):
        """
        Function that checks if a character is within self.word

        Parameters:
            char(str): An inputed character

        Returns:
            if char is in self.word, return the character in its correct position in self.puzzle
            if not, return a False value
        """
        """for item in self.word.lower():
            if item == char:
                return self.update_word_display() 
    
        return False"""
    
    def update_word_display(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guesses:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        self.word_display.set(displayed_word.strip())

        if all(letter in self.guesses for letter in self.word):
            messagebox.showinfo("Congratulations", "You won!")
            self.restart()

        elif self.attempts_left == 0:
            messagebox.showinfo("Game Over", f"You lost. The word was '{self.word}'.")
            self.restart()

        else:
            if self.guesses[-1] not in self.word:
                self.attempts_left -= 1
                self.draw_gallows()
        
    def check_guess(self):          #checks if guess if a valid input and appends to guesses list
        guess = self.guess_entry.get()
        if guess and guess.isalpha() and len(guess) == 1:
            if guess not in self.guesses:
                self.guesses.append(guess)
                self.update_word_display()
            else:
                messagebox.showinfo("Invalid Guess", "You've already guessed that letter.")
        else:
            messagebox.showinfo("Invalid Guess", "Please enter a single alphabetical character.")
        self.guess_entry.delete(0, tk.END)
