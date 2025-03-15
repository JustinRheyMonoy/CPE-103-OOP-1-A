import tkinter as tk
import math

# Functions for calculation
def get_input():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        return num1, num2
    except ValueError:
        result.set("Invalid input!")
        return None, None

def add():
    num1, num2 = get_input()
    if num1 is not None:
        res = num1 + num2
        result.set(res)
        update_history(f"{num1} + {num2} = {res}")

def subtract():
    num1, num2 = get_input()
    if num1 is not None:
        res = num1 - num2
        result.set(res)
        update_history(f"{num1} - {num2} = {res}")

def multiply():
    num1, num2 = get_input()
    if num1 is not None:
        res = num1 * num2
        result.set(res)
        update_history(f"{num1} × {num2} = {res}")

def divide():
    num1, num2 = get_input()
    if num1 is not None:
        if num2 == 0:
            result.set("Error! Division by zero.")
        else:
            res = num1 / num2
            result.set(res)
            update_history(f"{num1} ÷ {num2} = {res}")

def square():
    num1, _ = get_input()
    if num1 is not None:
        res = num1 ** 2
        result.set(res)
        update_history(f"{num1}² = {res}")

def square_root():
    num1, _ = get_input()
    if num1 is not None:
        if num1 < 0:
            result.set("Error! Negative square root.")
        else:
            res = math.sqrt(num1)
            result.set(res)
            update_history(f"√{num1} = {res}")

def power():
    num1, num2 = get_input()
    if num1 is not None:
        res = num1 ** num2
        result.set(res)
        update_history(f"{num1} ^ {num2} = {res}")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")

def update_history(operation):
    history_list.insert(tk.END, operation)

# Create the main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x600")
root.configure(bg="white")

# Enable dynamic resizing
for i in range(9):
    root.grid_rowconfigure(i, weight=1)
for i in range(2):
    root.grid_columnconfigure(i, weight=1)

# Create StringVar to hold the result
result = tk.StringVar()

# Layout components
tk.Label(root, text="Enter first number:", font=("Arial", 12, "bold"), fg="black").grid(row=0, column=0, sticky="w")
entry1 = tk.Entry(root, font=("Arial", 12))
entry1.grid(row=0, column=1, sticky="ew")

tk.Label(root, text="Enter second number:", font=("Arial", 12, "bold"), fg="black").grid(row=1, column=0, sticky="w")
entry2 = tk.Entry(root, font=("Arial", 12))
entry2.grid(row=1, column=1, sticky="ew")

# Buttons for operations
tk.Button(root, text="Add", command=add, fg="blue", font=("Arial", 12)).grid(row=2, column=0, sticky="nsew")
tk.Button(root, text="Subtract", command=subtract, fg="red", font=("Arial", 12)).grid(row=2, column=1, sticky="nsew")
tk.Button(root, text="Multiply", command=multiply, fg="green", font=("Arial", 12)).grid(row=3, column=0, sticky="nsew")
tk.Button(root, text="Divide", command=divide, fg="navy", font=("Arial", 12)).grid(row=3, column=1, sticky="nsew")
tk.Button(root, text="Square", command=square, fg="purple", font=("Arial", 12)).grid(row=4, column=0, sticky="nsew")
tk.Button(root, text="Square Root", command=square_root, fg="orange", font=("Arial", 12)).grid(row=4, column=1, sticky="nsew")
tk.Button(root, text="Power (x^y)", command=power, fg="violet", font=("Arial", 12)).grid(row=5, column=0, sticky="nsew")

# Clear button
tk.Button(root, text="Clear", command=clear, font=("Arial", 12)).grid(row=5, column=1, sticky="nsew")

# Label to show result
tk.Label(root, text="Result:", font=("Arial", 14, "bold")).grid(row=6, column=0, sticky="w")
result_label = tk.Label(root, textvariable=result, font=("Arial", 14))
result_label.grid(row=6, column=1, sticky="ew")

# History feature
tk.Label(root, text="Calculation History:", font=("Arial", 12, "bold")).grid(row=7, column=0, columnspan=2, sticky="w")
history_list = tk.Listbox(root, height=6, width=40, font=("Arial", 12))
history_list.grid(row=8, column=0, columnspan=2, sticky="nsew")

# Start the main loop
root.mainloop()
