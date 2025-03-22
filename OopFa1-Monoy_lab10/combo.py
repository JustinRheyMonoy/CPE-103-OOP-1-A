import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Creating tkinter window and setting dimensions
window = tk.Tk()
window.title('Birthdate Selector')
window.geometry('400x400')
window.configure(bg="light blue")
window.iconbitmap('calendar.ico')
main_frame = ttk.Frame(window, padding=30)
main_frame.pack(pady=35)

def centerWindow(self):
    screen = QApplication.primaryScreen().geometry()
    x = (screen.width() - self.width()) // 2
    y = (screen.height() - self.height()) // 2
    self.move(x, y)


def show_birth_info():
    selected_month = month_var.get()
    selected_day = day_var.get()
    selected_year = year_var.get()
    selected_gender = gender_var.get()

    if selected_month and selected_day and selected_year and selected_gender:
        showinfo("Birth Date Info",
                 f"Your birthdate: {selected_month} {selected_day}, {selected_year}\nGender: {selected_gender}")
    else:
        showinfo("Error", "Please select all birthdate fields.")

# Title Label
title_label = ttk.Label(main_frame, text="Select Your Birth Date",
                        background='light yellow', foreground="black",
                        font=("Times New Roman", 15), anchor="center", padding=10)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Month Selection
ttk.Label(main_frame, text="Month:", font=("Times New Roman", 12)).grid(row=1, column=0, sticky="w", pady=5)
month_var = tk.StringVar()
month = ttk.Combobox(main_frame, width=20, textvariable=month_var, state='readonly')
month['values'] = ('January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December')
month.grid(row=1, column=1, pady=5)

# Day Selection
ttk.Label(main_frame, text="Day:", font=("Times New Roman", 12)).grid(row=2, column=0, sticky="w", pady=5)
day_var = tk.StringVar()
day = ttk.Combobox(main_frame, width=20, textvariable=day_var, state="readonly")
day['values'] = tuple(range(1, 32))
day.grid(row=2, column=1, pady=5)

# Year Selection
ttk.Label(main_frame, text="Year:", font=("Times New Roman", 12)).grid(row=3, column=0, sticky="w", pady=5)
year_var = tk.StringVar()
year = ttk.Combobox(main_frame, width=20, textvariable=year_var, state="readonly")
year['values'] = tuple(range(1900, 2025))
year.grid(row=3, column=1, pady=5)

# Gender Selection
ttk.Label(main_frame, text="Gender:", font=("Times New Roman", 12)).grid(row=4, column=0, sticky="w", pady=5)
gender_var = tk.StringVar()
gender_frame = ttk.Frame(main_frame)
gender_frame.grid(row=4, column=1, pady=5)
ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left", padx=5)
ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left", padx=5)

# Show Info Button
style = ttk.Style()
style.configure("TButton", font=("Times New Roman", 12), padding=5)

ttk.Button(main_frame, text="Show Birth Info", command=show_birth_info, style="TButton").grid(row=5, column=0, columnspan=2, pady=15)

window.mainloop()
