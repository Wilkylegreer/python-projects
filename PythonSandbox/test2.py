import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Close', command=self.OnClosing)
        self.filemenu.add_separator()
        self.filemenu.add_command(
            label='Close Without Question', command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(
            label='Show Message', command=self.ShowMessage)

        self.menubar.add_cascade(menu=self.filemenu, label='File')
        self.menubar.add_cascade(menu=self.actionmenu, label='Action')

        self.root.config(menu=self.menubar)

        self.label = tk.Label(
            self.root, text='Your message', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, font=('Arial', 16))
        self.textbox.bind('<KeyPress>', self.Shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.checkState = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text='Show messagebox', font=(
            'Arial', 16), variable=self.checkState)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(
            self.root, text='Show message', font=('Arial', 18), command=self.ShowMessage)
        self.button.pack(padx=10, pady=10)

        self.clearBtn = tk.Button(
            self.root, text='Clear Box', font=('Arial', 18), command=self.Clear, fg='blue')
        self.clearBtn.pack(padx=10, pady=10)

        self.root.protocol('WM_DELETE_WINDOW', self.OnClosing)
        self.root.mainloop()

    def ShowMessage(self):
        if self.checkState.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(
                title="Message", message=self.textbox.get('1.0', tk.END))

    def Shortcut(self, event):
        if event.state == 12 and event.keysym == 'Return':
            self.ShowMessage()

    def OnClosing(self):
        if messagebox.askyesno(title='Quit?', message='Do you really want to quit?'):
            self.root.destroy()

    def Clear(self):
        self.textbox.delete('1.0', tk.END)


MyGUI()
