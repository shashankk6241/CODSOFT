import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        master.title("Simple Calculator")
        master.geometry("320x270")
        master.config(bg="#282c34")
        tk.Label(master, text="Simple Calculator", font=("Comic Sans MS",18,"bold"), bg="#282c34", fg="#61dafb").pack(pady=10)
        f = tk.Frame(master, bg="#282c34"); f.pack()
        tk.Label(f, text="Number 1:", bg="#282c34", fg="#61dafb", font=("Arial",12)).grid(row=0, column=0, padx=5)
        self.e1 = tk.Entry(f, width=10, bg="#20232a", fg="#61dafb")
        self.e1.grid(row=0,column=1, padx=5)
        tk.Label(f, text="Number 2:", bg="#282c34", fg="#61dafb", font=("Arial",12)).grid(row=1, column=0, padx=5, pady=15)
        self.e2 = tk.Entry(f, width=10, bg="#20232a", fg="#61dafb")
        self.e2.grid(row=1,column=1, padx=5, pady=15)
        self.op = tk.StringVar(value='+')
        tk.Label(master, text="Operation:", bg="#282c34", fg="#61dafb", font=("Arial",12)).pack()
        ops = ['+', '-', '*', '/']
        tk.OptionMenu(master, self.op, *ops).pack(pady=8)
        tk.Button(master, text="Calculate", bg="#21a1f1", fg="white", font=("Arial",12,"bold"), command=self.calculate).pack()
        self.result = tk.StringVar()
        tk.Label(master, textvariable=self.result, font=("Arial",13), bg="#282c34", fg="#61dafb", pady=15).pack()
    def calculate(self):
        try:
            n1, n2 = float(self.e1.get()), float(self.e2.get())
            o = self.op.get()
            v = {"+" : n1+n2, "-" : n1-n2, "*" : n1*n2}
            if o == "/": self.result.set(f"{n1} ÷ {n2} = {n1/n2}" if n2!=0 else "Error: Div by 0")
            else: self.result.set(f"{n1} {o} {n2} = {v[o]}")
        except Exception: self.result.set("Error: Enter valid numbers")

root = tk.Tk(); CalculatorApp(root); root.mainloop()
