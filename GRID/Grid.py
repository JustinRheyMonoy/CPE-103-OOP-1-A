from tkinter import *

from PyQt5.QtWidgets import QScrollBar

window = Tk()
window.title("Using grid manager")
window.geometry("400x200")

yscroll=Scrollbar(window)
yscroll.pack(side = RIGHT, fill = Y)

listbox = Listbox(window)
listbox.pack(side = LEFT, fill = BOTH, expand=True)

for x in range(51):
    listbox.insert(END, x)

listbox.config(yscrollcommand=yscroll.set)
yscroll.config(command=listbox.yview)

window.mainloop()