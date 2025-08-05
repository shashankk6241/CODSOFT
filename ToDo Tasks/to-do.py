import tkinter as tk
from tkinter import messagebox, simpledialog, font
import os

COLOR_BG = "#282c34"
COLOR_ACCENT = "#61dafb"
COLOR_BTN = "#21a1f1"
COLOR_BTN2 = "#d9534f"

class ToDoApp:
    def __init__(self, master):
        master.title("To-Do List")
        master.geometry("400x400")
        master.config(bg=COLOR_BG)
        tk.Label(master, text="My To-Do List", font=("Comic Sans MS", 20, "bold"), fg=COLOR_ACCENT, bg=COLOR_BG).pack(pady=10)
        self.tasks = self.load_tasks()
        f = tk.Frame(master, bg=COLOR_BG)
        f.pack(pady=10)
        self.listbox = tk.Listbox(f, width=40, height=12, font=("Arial", 12), fg=COLOR_ACCENT, bg="#20232a", selectbackground=COLOR_ACCENT)
        self.listbox.pack(side=tk.LEFT, padx=5)
        tk.Scrollbar(f, orient=tk.VERTICAL, command=self.listbox.yview).pack(side=tk.LEFT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.listbox.yview)
        self.refresh_listbox()
        bf = tk.Frame(master, bg=COLOR_BG)
        bf.pack(pady=10)
        tk.Button(bf, text="Add Task", font=("Arial",12,"bold"), bg=COLOR_BTN, fg="white", width=12, command=self.add_task).grid(row=0, column=0, padx=10)
        tk.Button(bf, text="Remove Selected", font=("Arial",12,"bold"), bg=COLOR_BTN2, fg="white", width=12, command=self.remove_task).grid(row=0, column=1, padx=10)

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for t in self.tasks:
            self.listbox.insert(tk.END, t)

    def add_task(self):
        t = simpledialog.askstring("Add Task", "Enter your task:")
        if t and t.strip():
            self.tasks.append(t.strip())
            self.refresh_listbox()
            self.save_tasks()

    def remove_task(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("No selection", "Select a task to remove.")
            return
        self.tasks.pop(sel[0])
        self.refresh_listbox()
        self.save_tasks()

    def save_tasks(self):
        with open("todo.txt", "w") as f:
            for t in self.tasks:
                f.write(t + "\n")
    def load_tasks(self):
        if os.path.exists("todo.txt"):
            with open("todo.txt") as f:
                return [x.strip() for x in f]
        return []

root = tk.Tk(); ToDoApp(root); root.mainloop()
