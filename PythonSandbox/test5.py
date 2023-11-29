import tkinter as tk


def move_selected_item():
    selected_item = listbox1.get(listbox1.curselection())
    listbox2.insert(tk.END, selected_item)
    listbox1.delete(listbox1.curselection())


root = tk.Tk()
root.title("Bulk File Renamer")

# Set the window size to 500x500 and disable resizing
root.geometry("500x500")
root.resizable(False, False)

# Create a label for the title
title_label = tk.Label(root, text="Bulk File Renamer", font=("Helvetica", 18))
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the first Listbox on the left
listbox1 = tk.Listbox(root, selectmode=tk.SINGLE)
listbox1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Create the second Listbox on the right
listbox2 = tk.Listbox(root, selectmode=tk.SINGLE)
listbox2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Create a frame to hold the buttons and entry
button_frame = tk.Frame(root)
button_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create Button 1
button1 = tk.Button(button_frame, text="Button 1")
button1.pack(side=tk.LEFT, padx=5, pady=5)

# Create an Entry field under Button 1
entry1 = tk.Entry(button_frame)
entry1.pack(side=tk.LEFT, padx=5, pady=5)

# Create Button 2
button2 = tk.Button(button_frame, text="Button 2")
button2.pack(side=tk.LEFT, padx=5, pady=5)

# Add some sample items to listbox1
for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
    listbox1.insert(tk.END, item)

# Create a button to move selected item from listbox1 to listbox2
move_button = tk.Button(root, text="Move ->", command=move_selected_item)
move_button.grid(row=3, column=0, columnspan=2, pady=5)

# Configure column and row weights for resizing
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

root.mainloop()
