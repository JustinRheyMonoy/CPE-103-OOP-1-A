import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("320x425")
root.configure(bg='#300a0a')
display_frame = tk.Frame(root, bd=10, bg='#403838', )
display_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

entry = tk.Entry(display_frame, font=('Arial', 28), fg = 'white', bg='#300a0a', justify='right')
entry.pack(fill='both', expand=True)

def on_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + char)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

buttons = [
    ('C', 1, 0, 3, clear, ),
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
    ('-', 4, 3, 1, lambda: on_click('-')),

    ('.', 5, 0, 1, lambda: on_click('.')), 
    ('0', 5, 1, 1, lambda: on_click('0')), 
    ('+', 3, 3, 1, lambda: on_click('+')),


    ('=', 5, 2, 2, calculate)
]

for (text, row, col, colspan, cmd) in buttons:
    btn = tk.Button(root, text=text, font=('Arial', 15), width=4, height=2, command=cmd, fg = 'white', bg = '#403838')
    btn.grid(row=row, column=col, columnspan=colspan, padx=1, pady=1, sticky='nesw')



for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=2)

root.mainloop()