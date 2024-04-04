import random
import tkinter as tk
from tkinter import messagebox, colorchooser
import statistics

class MathGame:
    def __init__(self, parent):
        self.parent = parent
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.total_questions = 0
        self.user_inputs = []  # List to store user inputs
        self.correct_answers_list = []  # List to store corresponding correct answers
        self.correctly_answered_list = []  # List to store correctly answered answers
        self.question_label = None
        self.entry = None
        self.stats_label = None
        self.correct_answer = None
        self.setup_gui()

    def generate_question(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
        question = f"What is {num1} {operator} {num2}?"
        return question, answer

    def check_answer(self):
        user_answer = self.entry.get()
        self.user_inputs.append(user_answer)  # Add user input to the list
        self.entry.delete(0, tk.END)
        try:
            user_answer = int(user_answer)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        if user_answer == self.correct_answer:
            messagebox.showinfo("Correct", "You Are Correct!")
            self.correctly_answered_list.append(self.correct_answer) # Add correctly given answer to the list
            self.correct_answers_list.append(self.correct_answer)  # Add correct answer to the list
            self.update_stats(True)
        else:
            messagebox.showerror("Incorrect", f"Incorrect. The correct answer is {self.correct_answer}.")
            self.update_stats(False)
            self.correct_answers_list.append(self.correct_answer)  # Add correct answer to the list

    def update_stats(self, correct):
        if correct:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1
        self.total_questions += 1
        percentage_correct = (self.correct_answers / self.total_questions) * 100 if self.total_questions > 0 else 0

        if self.correctly_answered_list:  # Check if the list is not empty
            mean = statistics.mean(self.correctly_answered_list)
            mode = statistics.mode(self.correctly_answered_list)
            median = statistics.median(self.correctly_answered_list)

        self.stats_label.config(text=f"Correct Answers: {self.correct_answers}, Incorrect Answers: {self.incorrect_answers}, Percentage Correct: {percentage_correct:.2f}%, \n Correct Answers Given: Mean: {mean}, Mode: {mode}, Median: {median}")
        self.next_question()

    def next_question(self):
        question, self.correct_answer = self.generate_question()
        self.question_label.config(text=question)

    def setup_gui(self):
        self.question_label = tk.Label(self.parent, text="", font=("Arial", 14), bg="cyan")
        self.question_label.pack(pady=10)

        self.entry = tk.Entry(self.parent, font=("Arial", 14), bg="cyan")
        self.entry.pack(pady=5)

        check_button = tk.Button(self.parent, text="Check Your Answer", command=self.check_answer, bg="sky blue")
        check_button.pack(pady=5)

        self.stats_label = tk.Label(self.parent, text="", bg="cyan")
        self.stats_label.pack(pady=10)

        self.next_question()

    def add_user_input(self):
        return self.user_inputs

    def add_correct_answer(self):
        return self.correct_answers_list

    def add_correct_answer_answered(self):
        return self.correctly_answered_list

def main():
    root = tk.Tk()
    root.title("Rozha's Math Game")
    root.config(bg="cyan")  # Set background color to cyan
    game = MathGame(root)

    def on_continue():
        if messagebox.askyesno("Continue", "Do you want to continue?"):
            game.next_question()
        else:
            print("User inputs:", game.add_user_input())
            print("Correct answers:", game.add_correct_answer())
            print("Correct answers given:", game.add_correct_answer_answered())
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_continue)
    root.mainloop()

if __name__ == "__main__":
    main()
