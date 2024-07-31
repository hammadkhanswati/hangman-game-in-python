import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.word_list = ['PYTHON', 'JAVA', 'KOTLIN', 'JAVASCRIPT', 'SWIFT']
        self.word = random.choice(self.word_list)
        self.guessed_word = ["_"] * len(self.word)
        self.guesses_left = 6
        self.guessed_letters = set()
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.root, text=" ".join(self.guessed_word), font=("Helvetica", 24))
        self.label.pack(pady=20)
        
        self.entry = tk.Entry(self.root, font=("Helvetica", 18))
        self.entry.pack(pady=20)
        
        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess, font=("Helvetica", 18))
        self.guess_button.pack(pady=20)
        
        self.status_label = tk.Label(self.root, text=f"Guesses left: {self.guesses_left}", font=("Helvetica", 18))
        self.status_label.pack(pady=20)
        
    def make_guess(self):
        guess = self.entry.get().upper()
        self.entry.delete(0, tk.END)
        
        if not guess.isalpha() or len(guess) != 1:
            messagebox.showwarning("Invalid input", "Please enter a single letter.")
            return
        
        if guess in self.guessed_letters:
            messagebox.showwarning("Duplicate guess", "You already guessed that letter.")
            return
        
        self.guessed_letters.add(guess)
        
        if guess in self.word:
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.guessed_word[idx] = guess
            self.label.config(text=" ".join(self.guessed_word))
        else:
            self.guesses_left -= 1
            self.status_label.config(text=f"Guesses left: {self.guesses_left}")
        
        if "_" not in self.guessed_word:
            messagebox.showinfo("Hangman", "Congratulations! You won!")
            self.root.destroy()
        elif self.guesses_left == 0:
            messagebox.showinfo("Hangman", f"You lost! The word was {self.word}.")
            self.root.destroy()

# Main code to run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
