import tkinter as tk 
from math import sin, cos, exp, radians

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("320x480")
root.configure(bg='#300a0a')
title_label = tk.Label(root, text="Scientific Calculator", font=('Arial', 20, 'bold'), fg='white', bg='#300a0a')
title_label.grid(row=0, column=0, columnspan=4, pady=15)


display_frame = tk.Frame(root, bd=20, bg='#403838', )
display_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=10, sticky='nsew')

entry = tk.Entry(display_frame, font=('Arial', 48), fg = 'white', bg='#300a0a', justify='right')
entry.pack(fill='both', expand=True)

def on_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + char)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def calc_sin():
    try:
        result = sin(radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def calc_cos():
    try:
        result = cos(radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def calc_square():
    try:
        value = float(entry.get())
        result = value ** 2
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def clear():
    entry.delete(0, tk.END)

menu = tk.Menu(root)
root.config(menu=menu)
edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear", command=clear)

buttons = [
    
    ('C', 5, 2, 1, clear, ),
    ('x²', 1, 0, 1, calc_square),
    ('sin', 1, 1, 1, calc_sin),
    ('cos', 1, 2, 1, calc_cos),
    ('7', 2, 0, 1, lambda: on_click('7')), 
    ('8', 2, 1, 1, lambda: on_click('8')), 
    ('9', 2, 2, 1, lambda: on_click('9')), 
    ('/', 1, 3, 1, lambda: on_click('/')),

    ('4', 3, 0, 1, lambda: on_click('4')), 
    ('5', 3, 1, 1, lambda: on_click('5')), 
    ('6', 3, 2, 1, lambda: on_click('6')), 
    ('*', 2, 3, 1, lambda: on_click('*')),

    ('1', 4, 0, 1, lambda: on_click('1')), 
    ('2', 4, 1, 1, lambda: on_click('2')), 
    ('3', 4, 2, 1, lambda: on_click('3')), 
    ('-', 3, 3, 1, lambda: on_click('-')),

    ('.', 5, 0, 1, lambda: on_click('.')), 
    ('0', 5, 1, 1, lambda: on_click('0')), 
    ('+', 4, 3, 1, lambda: on_click('+')),


    ('=', 5, 3, 1, calculate)
]

for (text, row, col, colspan, cmd) in buttons:
    btn = tk.Button(root, text=text, font=('Arial', 12), width=4, height=2, command=cmd, fg = 'white', bg = '#403838')
    btn.grid(row=row, column=col, columnspan=colspan, padx=1, pady=1, sticky='nsew')



for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()