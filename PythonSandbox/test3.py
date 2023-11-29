import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

window = tk.Tk()
window.title('buttons')
window.geometry('600x400')


def ButtonFunc():
    print('A basic button')


# Basic Button
button = ttk.Button(window, text='A simple button', command=ButtonFunc)
button.pack()

# Check Button
checkVar = tk.IntVar(value=10)  # Set default
check = ttk.Checkbutton(window, text='Checkbox 1', command=lambda: print(
    checkVar.get()), variable=checkVar, onvalue=10, offvalue=5)
check.pack()

# Radio Button
radio1 = ttk.Radiobutton(window, text='Radiobutton 1', value='radio2')
radio1.pack()
radio2 = ttk.Radiobutton(window, text='Radiobutton 2', value='radio1')
radio2.pack()

window.mainloop()
