import tkinter as tk

class Gallows:
    def __init__(self, master):
        self.x0 = 50 
        self.y0 = 280
        self.x1 = 150 
        self.y1 = 280
        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()

    def draw_gallows(self):
        self.canvas.create_line(self.x0, self.y0, self.x1, self.y1, tags="hangman")      # Bottom line
        self.canvas.create_line(self.x0 + 50, self.y0, self.x1 + 50, self.y1, tags="hangman")  # Vertical line
        self.canvas.create_line(self.x0, self.y0 - 300, self.x0, self.y0, tags="hangman")  # Left vertical line
        self.canvas.create_line(self.x1, self.y0 - 250, self.x1, self.y0 - 220, tags="hangman")  # Right vertical line

    def head(self):
        head_radius = 25
        head_center_x = self.x1
        head_center_y = self.y0 - 195
        self.canvas.create_oval(
            head_center_x - head_radius, head_center_y - head_radius,
            head_center_x + head_radius, head_center_y + head_radius, tags="hangman"
        )

    def body(self):
        self.canvas.create_line(self.x1, self.y0 - 170, self.x1, self.y0 - 68, tags="hangman")

    def left_arm(self):
        self.canvas.create_line(self.x1, self.y0 - 170, self.x1 - 50, self.y0 - 150, tags="hangman")

    def right_arm(self):
        self.canvas.create_line(self.x1, self.y0 - 170, self.x1 + 50, self.y0 - 150, tags="hangman")

    def left_leg(self):
        self.canvas.create_line(self.x1, self.y0 - 75, self.x1 - 25, self.y0, tags="hangman")

    def right_leg(self):
        self.canvas.create_line(self.x1, self.y0 - 75, self.x1 + 25, self.y0, tags="hangman")

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