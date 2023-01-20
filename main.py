import tkinter as tk
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()
    with open(filepath, 'r') as file:
        text.insert('1.0', file.read())

def save_file():
    filepath = filedialog.asksaveasfilename()
    with open(filepath, 'w') as file:
        file.write(text.get('1.0', 'end'))

root = tk.Tk()
root.title("Notepad")

text = tk.Text(root)
text.pack()

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.mainloop()
