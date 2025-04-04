import tkinter as tk
import random


def play(user_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Computer chose {computer_choice}. {result}")


# GUI Setup
root = tk.Tk()
root.title("Rock-Paper-Scissors")

tk.Label(root, text="Choose Rock, Paper, or Scissors:").pack()

tk.Button(root, text="Rock", width=15,
          command=lambda: play("rock")).pack(pady=2)
tk.Button(root, text="Paper", width=15,
          command=lambda: play("paper")).pack(pady=2)
tk.Button(root, text="Scissors", width=15,
          command=lambda: play("scissors")).pack(pady=2)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()
