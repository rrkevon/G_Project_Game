import random
import tkinter as tk
from tkinter import simpledialog, messagebox, colorchooser

class SnakesAndLadders:
    def __init__(self):
        self.snake_squares = {16: 4, 22:10, 33: 20, 48: 24, 62: 56, 78: 69, 74: 60, 91: 42, 97: 6}
        self.ladder_squares = {3: 12, 7: 23, 11:25, 21: 56, 47: 53, 60: 72, 80: 96}
        self.num_cells = 100
        self.num_snake_squares = len(self.snake_squares)
        self.snake_probability = self.calculate_snake_probability(self.num_snake_squares, self.num_cells)
        self.root = tk.Tk()
        self.root.withdraw()

    def calculate_snake_probability(self, num_snakes, total_squares):
        return num_snakes / total_squares

    def move(self, player, value):
        throw = random.randint(1, 6)
        num = value + throw
        if num > 100:
            messagebox.showinfo("Game Message", "Bad luck! You can't move. You need a {} to win.".format(100 - value))
            return value
        if num == 100:
            return num
        messagebox.showinfo("Game Message", "{} rolled a {} and is now on square {}".format(player, throw, num))
        if num in self.snake_squares:
            num = self.snake_squares[num]
            messagebox.showinfo("Game Message", "{} got bitten by a snake and is now on square {}".format(player, num))
        elif num in self.ladder_squares:
            num = self.ladder_squares[num]
            messagebox.showinfo("Game Message", "{} climbed a ladder and is now on square {}".format(player, num))
        return num

    def players_count(self):
        while True:
            try:
                num_of_players = simpledialog.askinteger("Player Count", "How many players are in the game?", minvalue=2, maxvalue=4)
                if num_of_players is None:
                    messagebox.showinfo("Game Message", "Game cancelled.")
                    self.root.destroy()
                    return None
                return num_of_players
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a number between 2 and 4.")
                continue

    def names_of_players(self, num):
        names = []
        for i in range(num):
            name = simpledialog.askstring("Player Name", "What is the name of Player {}?".format(i + 1))
            if name is None:
                messagebox.showinfo("Game Message", "Game cancelled.")
                self.root.destroy()
                return None
            names.append(name)
        return names

    def turn(self, player, pos, game_over):
        def stop():
            game_over[0] = True
            self.root.quit()

        self.root = tk.Tk()
        self.root.title("Snakes and Ladders")
        self.root.geometry("300x100")

        # Set background color to cyan
        self.root.config(bg="cyan")
        
        # Calculate the current probability and display
        lbl_prob = tk.Label(self.root, text=f"Probability of landing on a snake: {self.snake_probability: .2f}", bg="cyan")
        lbl_prob.pack()

        lbl = tk.Label(self.root, text=f"Hey {player}! It's your turn now", bg="cyan")
        lbl.pack()

        btn_roll = tk.Button(self.root, text="Roll Dice", command=self.root.quit, bg="sky blue")
        btn_roll.pack(side=tk.LEFT, padx=10)

        btn_stop = tk.Button(self.root, text="Stop", command=stop, bg="sky blue")
        btn_stop.pack(side=tk.LEFT, padx=10)

        self.root.mainloop()
        self.root.destroy()

        if game_over[0]:
            return True, pos

        pos = self.move(player, pos)
        if pos == 100:
            messagebox.showinfo("Game Message", f"{player} WINS THE GAME! CONGRATULATIONS")
            return True, pos
        return False, pos

    def gmain(self):
        num_of_players = self.players_count()
        if num_of_players is None:
            return
        player_names = self.names_of_players(num_of_players)
        if player_names is None:
            return
        messagebox.showinfo("Game Message", "{} - Welcome To Snakes And Ladders".format(", ".join(player_names)))
        turns = 0
        positions = [1] * num_of_players
        game_over = [False]
        while not game_over[0]:      
            while turns < num_of_players:
                turns += 1
                game_over[0], positions[turns - 1] = self.turn(player_names[turns - 1], positions[turns - 1], game_over)
                if game_over[0]:
                    return
            turns = 0

def main():
    game = SnakesAndLadders()
    game.gmain()

if __name__ == '__main__':
    main()
