# Tkinter is Python's Graphical User Interface (GUI) package.
# It's a great way for beginners to start creating visual apps with Python.

import tkinter as tk


def say_hello():
    name = name_entry.get()

    if name:
        greeting_label.config(text=f"Hello, {name}")
    else:
        greeting_label.config(text="Hello, World")


window = tk.Tk()
window.title("My First Tkinter Hello World App")
window.geometry("500x250")
window.resizable(False, False)

title_label = tk.Label(window, text="Welcome to Tkinter!", font=("Arial", 16))
title_label.pack(pady=10)

name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=10)

hello_button = tk.Button(window, text="Say Hello", command=say_hello)
hello_button.pack(pady=10)

greeting_label = tk.Label(window, text="", font=("Arial", 12))
greeting_label.pack(pady=10)

window.mainloop()
