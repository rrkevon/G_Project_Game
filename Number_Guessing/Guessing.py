import random
import tkinter as tk
from tkinter import messagebox, colorchooser

class NumberGuessingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("300x150")
        
        self.lower_bound = 1
        self.upper_bound = 100
        self.secret_number = random.randint(self.lower_bound, self.upper_bound)
        self.attempts = 0
        self.max_attempts = 5

        # Set background color to cyan
        self.master.config(bg="cyan")

        self.label = tk.Label(master, text="Guess a number between 1 and 100:", bg="cyan", )
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_guess, bg="sky blue")
        self.submit_button.pack()

    def check_guess(self):
        self.attempts += 1
        guess = str(self.entry.get())
        #checks to see if the user entered a string and outputs and error message if such is the case
        try:
            guess = int(guess)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return        
        
        if guess == self.secret_number:
            messagebox.showinfo("Congratulations!", f"You guessed the secret number {self.secret_number} in {self.attempts} attempts.")
            self.master.destroy()
        elif guess < self.secret_number:
            messagebox.showinfo("Too low", "Try a higher number!")
        else:
            messagebox.showinfo("Too high", "Try a lower number!")
        
        if self.attempts >= self.max_attempts:
            messagebox.showinfo("Game Over", f"Sorry, you ran out of attempts! The secret number was {self.secret_number}.")
            self.master.destroy()

def main():
    root = tk.Tk()
    app = NumberGuessingGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
