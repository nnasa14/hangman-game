import tkinter as tk
from tkinter import messagebox
import json
import random

class Hangman:
    """
    A class of functions that fulfil the rules of a Hangman game
    """
    def __init__(self, master):
        self.master = master
        with open("words.json", 'r') as file:
            self.word_list = json.load(file)
        self.word = ""
        self.letters_guessed = []
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
        x0, y0 = 50, 280
        x1, y1 = 150, 280

        # Draw the main structure
        if self.attempts_left < self.max_attempts:
            self.canvas.create_line(x0, y0, x1, y1, tags="hangman")      # Bottom line
            self.canvas.create_line(x0 + 50, y0, x1 + 50, y1, tags="hangman")  # Vertical line
            self.canvas.create_line(x0, y0 - 300, x0, y0, tags="hangman")  # Left vertical line
            self.canvas.create_line(x1, y0 - 250, x1, y0 - 220, tags="hangman")  # Right vertical line

        # Draw the head
        if self.attempts_left < self.max_attempts - 1:
            head_radius = 25
            head_center_x = x1
            head_center_y = y0 - 195
            self.canvas.create_oval(
                head_center_x - head_radius, head_center_y - head_radius,
                head_center_x + head_radius, head_center_y + head_radius, tags="hangman"
            )

        # Draw the body
        if self.attempts_left < self.max_attempts - 2:
            self.canvas.create_line(x1, y0 - 170, x1, y0 - 68, tags="hangman")

        # Draw the left arm
        if self.attempts_left < self.max_attempts - 3:
            self.canvas.create_line(x1, y0 - 170, x1 - 50, y0 - 150, tags="hangman")

        # Draw the right arm
        if self.attempts_left < self.max_attempts - 4:
            self.canvas.create_line(x1, y0 - 170, x1 + 50, y0 - 150, tags="hangman")

        # Draw the left leg
        if self.attempts_left < self.max_attempts - 5:
            self.canvas.create_line(x1, y0 - 75, x1 - 25, y0, tags="hangman")

        # Draw the right leg
        if self.attempts_left < self.max_attempts - 6:
            self.canvas.create_line(x1, y0 - 75, x1 + 25, y0, tags="hangman")

    def restart(self):
        self.word_label.pack_forget()
        self.guess_entry.pack_forget()
        self.submit_button.pack_forget()
        self.restart_button.pack_forget()
        self.letters_guessed = []
        self.canvas.delete("hangman")
        self.start_game()
    
    def update_word_display(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.letters_guessed:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        self.word_display.set(displayed_word.strip())

        if all(letter in self.letters_guessed for letter in self.word):
            messagebox.showinfo("Congratulations", "You won!")
            self.restart()

        elif self.attempts_left == 0:
            self.attempts_left -= 1
            self.draw_gallows()
            self.master.update_idletasks()  # Update the display immediately
            messagebox.showinfo("Game Over", f"You lost. The word was '{self.word}'.")
            self.restart()

        else:
            if self.letters_guessed[-1] not in self.word:
                self.attempts_left -= 1
                self.draw_gallows()
        
    def check_guess(self):          # Checks if guess is a valid input and appends to guesses list
        guess = self.guess_entry.get()
        if len(guess) == 1:     # Guessing the character
            if guess.isalpha() and guess not in self.letters_guessed:
                self.letters_guessed.append(guess)
                self.update_word_display()
            elif guess.isalpha():
                messagebox.showinfo("Invalid Guess", "You've already guessed that letter.")
            else:
                messagebox.showinfo("Invalid Guess", "Please enter a single alphabetical character.")
        else:               # Guessing the word
            if guess == self.word:
                messagebox.showinfo("Congratulations", "You won!")
                self.restart()
            
            else:
                # FIXME: Immediate game over and fully drawn hangman upon incorrect guess.
                #self.draw_gallows()
                #self.master.update_idletasks()  # Update the display immediately
                messagebox.showinfo("Game Over", f"You lost. The word was '{self.word}'.")
                self.restart()
            if len(guess) < 2:
                messagebox.showinfo("Invalid Guess", "Please enter a single alphabetical character.")

        self.guess_entry.delete(0, tk.END)
