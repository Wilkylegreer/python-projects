import os
from CTkListbox import *
import customtkinter as tk
from customtkinter import filedialog

def Refresh():
    FakeRename()
    PreviewFiles()

def FakeRename():
    changeWindow.delete(0, tk.END)
    fakeFiles = files
    for y in range(len(fakeFiles)):
        fakeFiles[y] = prefixEntry.get() + str(y)
        changeWindow.insert(y, fakeFiles[y])

def PreviewFiles():
    global files
    files = []
    previewWindow.delete(0, tk.END)
    for filename in os.listdir(fP):
        files.append(filename)
    files = sorted(files, key=str.casefold)
    for x in range(len(files)):
        previewWindow.insert(x, files[x])
    FakeRename()

def OpenFile():
    global fP
    fP = filedialog.askdirectory()
    if fP:
        print("Selected Folder:", fP)
        PreviewFiles()
    else:
        print("No file selected")

def FileRename():
    filePaths = []
    for filename in os.listdir(fP):
        file_path = os.path.join(fP, filename)
        filePaths.append(file_path)
    for x in range(len(filePaths)):
        oldext = os.path.splitext(filePaths[x])[1]
        if os.path.isfile(file_path):
            newFilename = prefixEntry.get() + str(x) + oldext
            newFilePath = os.path.join(fP, newFilename)
            try:
                os.rename(filePaths[x], newFilePath)
            except:
                pass

# Create a custom tkinter window (optional)
root = tk.CTk()
root.title('File Renamer')

# Window Properties
windowWidth = 500
windowHeight = 500
displayWidth = root.winfo_screenwidth()
displayHeight = root.winfo_screenheight()

left = int(displayWidth / 2 - windowWidth / 2)
top = int(displayHeight / 2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{left}+{top}')

# Folder Icon
# root.iconbitmap('./Folder.ico')
root.resizable(False, False)

root.bind('<Escape>', lambda event: root.quit())

# Widget Creation
title = tk.CTkLabel(root, text='Bulk File Renamer',
                  font=('Arial', 20), fg_color='transparent')

buttonFrame = tk.CTkFrame(root)
buttonFrame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

buttonOpen = tk.CTkButton(buttonFrame, text='Open Folder', command=OpenFile)
buttonRefresh = tk.CTkButton(buttonFrame, text='Refresh', command=Refresh)
prefixEntry = tk.CTkEntry(buttonFrame)
buttonVerify = tk.CTkButton(buttonFrame, text='OK', command=FileRename)

previewWindow = CTkListbox(root, font=('Arial', 8), height=20)
changeWindow = CTkListbox(root, font=('Arial', 8), height=20)

previewWindow.insert(0, 'No Folder Selected')
changeWindow.insert(0, 'No Folder Selected')

# Layout
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

buttonOpen.pack(side=tk.LEFT, padx=5, pady=5)
buttonRefresh.pack(side=tk.LEFT, padx=5, pady=5)
prefixEntry.pack(side=tk.LEFT, padx=5, pady=5)
buttonVerify.pack(side=tk.LEFT, padx=5, pady=5)

previewWindow.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
changeWindow.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Config
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

root.mainloop()
