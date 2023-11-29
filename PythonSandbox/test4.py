import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Combined Layout')
root.geometry('600x600')
root.minsize(600, 600)

menuFrame = ttk.Frame(root)
mainFrame = ttk.Frame(root)

menuFrame.place(x=0, y=0, relwidth=0.3, relheight=1)
mainFrame.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

# Menu Widgets
menuButton1 = ttk.Button(menuFrame, text='Button1')
menuButton2 = ttk.Button(menuFrame, text='Button2')
menuButton3 = ttk.Button(menuFrame, text='Button3')

# Menu layout
menuFrame.columnconfigure((0, 1, 2), weight=1, uniform='a')
menuFrame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

menuButton1.grid(row=0, column=0, sticky='nswe', columnspan=2)
menuButton2.grid(row=0, column=2, sticky='nswe')
menuButton3.grid(row=1, column=0, sticky='nswe', columnspan=3)

root.mainloop()
