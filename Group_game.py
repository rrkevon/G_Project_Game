import tkinter as tk
from tkinter import messagebox
from tkinter import colorchooser
import subprocess

class GameLauncher:
    def __init__(self, master):
        self.master = master
        self.master.title("Game Launcher")
        self.master.geometry("300x200")
        
        # Set background color to cyan
        self.master.config(bg="cyan")                      

        self.label = tk.Label(master, text="Select a game to play:", bg="red")
        self.label.pack()

        self.math_game_button = tk.Button(master, text="Math Game", command=self.launch_math_game, bg="white")
        self.math_game_button.pack()

        self.number_guessing_button = tk.Button(master, text="Number Guessing Game", command=self.launch_number_guessing, bg="white")
        self.number_guessing_button.pack()

        self.snake_and_ladder_button = tk.Button(master, text="Snake and Ladder", command=self.launch_snake_and_ladder, bg="white")
        self.snake_and_ladder_button.pack()

    def launch_math_game(self):
        try:
            subprocess.run(["python", "-m", "Math_Game.MathGame"])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def launch_number_guessing(self):
        try:
            subprocess.run(["python", "-m", "Number_Guessing.Guessing"])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def launch_snake_and_ladder(self):
        try:
            subprocess.run(["python", "-m", "Snake_and_Ladder.Snakeandladders"])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = GameLauncher(root)
    root.mainloop()

if __name__ == "__main__":
    main()
