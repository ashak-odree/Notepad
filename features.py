import tkinter as tk
from tkinter import filedialog, font

def open_file():
    filepath = filedialog.askopenfilename()
    with open(filepath, 'r') as file:
        text.insert('1.0', file.read())

def save_file():
    filepath = filedialog.asksaveasfilename()
    with open(filepath, 'w') as file:
        file.write(text.get('1.0', 'end'))

def set_font():
    font_options = font.Font(family='Arial', size=12)
    text.config(font=font_options)

def set_background_color():
    color = filedialog.askcolor()
    text.config(bg=color[1])

root = tk.Tk()
root.title("Notepad")

text = tk.Text(root)
text.pack()

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = tk.Menu(menubar)
editmenu.add_command(label="Cut", command=lambda: text.event_generate("<<Cut>>"))
editmenu.add_command(label="Copy", command=lambda: text.event_generate("<<Copy>>"))
editmenu.add_command(label="Paste", command=lambda: text.event_generate("<<Paste>>"))
menubar.add_cascade(label="Edit", menu=editmenu)

viewmenu = tk.Menu(menubar)
viewmenu.add_command(label="Font", command=set_font)
viewmenu.add_command(label="Background Color", command=set_background_color)
menubar.add_cascade(label="View", menu=viewmenu)

root.config(menu=menubar)

text.bind("<Control-z>", lambda event: text.edit_undo())
text.bind("<Control-y>", lambda event: text.edit_redo())

root.mainloop()
