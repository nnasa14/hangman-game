from Hangman import Hangman
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hangman")
    hangman_instance = Hangman(root)
    root.mainloop()

# TODO: add list of wrong guesses
# TODO: add guess word funct to hangman.py