import tkinter as tk
from tkinter import ttk

class SimpleCalculator:


    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.config(bg="#ffffff")
        
        self.result_var = tk.StringVar(value="0")
        self.result_label = tk.Label(root, textvariable=self.result_var, font=("Helvetica", 24), bg="#ffffff")
        self.result_label.grid(row=0, column=0, columnspan=4, pady=20)

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        for i, text in enumerate(button_texts):
            col = i % 4
            row = i // 4 + 1
            button = ttk.Button(self.root, text=text, command=lambda t=text: self.on_button_click(t), style="Calculator.TButton")
            button.grid(row=row, column=col, padx=10, pady=10)

    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
                
                # Write the result in plain text
                with open("results.txt", "a") as f:
                    f.write(f"{self.result_var.get()}\n")
                    
            except:
                self.result_var.set("Error")
        elif text == "C":
            self.result_var.set("0")
        else:
            current = self.result_var.get()
            if current == "0":
                current = ""
            self.result_var.set(current + text)


root = tk.Tk()
style = ttk.Style(root)
style.configure("Calculator.TButton", background="#ffffff", foreground="#333333", font=("Helvetica", 14))

calculator = SimpleCalculator(root)
root.mainloop()