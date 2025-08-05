import tkinter as tk
import random

class RPSGameApp:
    def __init__(self, master):
        master.title("Rock Paper Scissors")
        master.geometry("440x370")
        master.config(bg="#282c34")
        tk.Label(master, text="Rock Paper Scissors", font=("Comic Sans MS",18,"bold"), fg="#61dafb", bg="#282c34").pack(pady=12)
        self.choices = ['Rock', 'Paper', 'Scissors']
        self.user_score = 0
        self.comp_score = 0
        bf = tk.Frame(master, bg="#282c34")
        bf.pack(pady=15)
        for c in self.choices:
            tk.Button(bf, text=c, width=12, font=("Arial",12,"bold"), bg="#007acc", fg="white", command=lambda C=c: self.play(C)).pack(side=tk.LEFT, padx=12)
        self.score = tk.StringVar(); self.score.set("User: 0       Computer: 0")
        tk.Label(master, textvariable=self.score, font=("Arial",14), fg="#61dafb", bg="#282c34").pack(pady=10)
        self.result = tk.StringVar()
        tk.Label(master, textvariable=self.result, font=("Arial",13), wraplength=380, fg="#61dafb", bg="#282c34").pack(pady=8)
        tk.Button(master, text="Reset Scores", font=("Arial",12,"bold"), bg="#d9534f", fg="white", width=15, command=self.reset).pack(pady=15)
    def play(self, us):
        comp = random.choice(self.choices)
        if us == comp: res = "It's a Tie!"
        elif (us == "Rock" and comp == "Scissors") or (us == "Paper" and comp == "Rock") or (us == "Scissors" and comp == "Paper"):
            res = "You Win!"; self.user_score += 1
        else: res = "You Lose!"; self.comp_score += 1
        self.score.set(f"User: {self.user_score}       Computer: {self.comp_score}")
        self.result.set(f"You chose {us}. Computer chose {comp}. {res}")
    def reset(self):
        self.user_score = 0; self.comp_score = 0
        self.score.set("User: 0       Computer: 0")
        self.result.set("Scores reset. Play again!")

root = tk.Tk(); RPSGameApp(root); root.mainloop()
