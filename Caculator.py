from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='First number')
        self.lbl2 = Label(win, text='Second number')
        self.lbl3 = Label(win, text='Result')

        self.t1 = Entry(bd=3)
        self.t2 = Entry()
        self.t3 = Entry()

        self.btn1 = Button(win, text='Add', command=self.add, fg="blue")
        self.btn2 = Button(win, text='Subtract', command=self.sub, fg="red")
        self.btn3 = Button(win, text='Multiply', command=self.multiply,  fg="green")
        self.btn4 = Button(win, text='Clear', command=self.clear, fg="black")

        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)

        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)

        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=150)

        self.btn1.place(x=105, y=200)
        self.btn2.place(x=155, y=200)
        self.btn3.place(x=230, y=200)
        self.btn4.place(x=185, y=250)

    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def multiply(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def clear(self):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')


window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()

