import tkinter as tk
from tkinter import colorchooser

current_x, current_y = 0, 0
color = "black"
pen_size = 5


def start_position(event):
    global current_x, current_y

    current_x, current_y = event.x, event.y


def draw_line(event):
    global current_x, current_y
    canvas.create_line(current_x, current_y, event.x, event.y,
                       fill=color, width=pen_size, capstyle=tk.ROUND, smooth=True)
    current_x, current_y = event.x, event.y


def change_color():
    global color
    new_color = colorchooser.askcolor()[1]
    if new_color:
        color = new_color


def use_eraser():
    global color
    color = "white"  # Same as canvas background


def clear_canvas():
    canvas.delete("all")


def change_pen_size(new_size):
    global pen_size
    pen_size = new_size


def set_small_pen():
    change_pen_size(2)


def set_medium_pen():
    change_pen_size(5)


def set_large_pen():
    change_pen_size(10)


# Main Window Loop

window = tk.Tk()
window.title("Tkinter Drawing App")
window.geometry("800x600")

title_label = tk.Label(window, text="Simple Drawing App", font=("Arial", 18))
title_label.pack(pady=10)

toolbar_frame = tk.Frame(window)
toolbar_frame.pack(fill=tk.X, pady=5)

color_button = tk.Button(
    toolbar_frame, text="Choose Color", command=change_color)
color_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(
    toolbar_frame, text="Clear Canvas", command=clear_canvas)
clear_button.pack(side=tk.LEFT, padx=5)

eraser_button = tk.Button(toolbar_frame, text="Eraser", command=use_eraser)
eraser_button.pack(side=tk.LEFT, padx=5)

size_frame = tk.Frame(toolbar_frame)
size_frame.pack(side=tk.LEFT, padx=15)

size_label = tk.Label(size_frame, text="Pen Size:")
size_label.pack(side=tk.LEFT)

small_button = tk.Button(size_frame, text="Small", command=set_small_pen)
small_button.pack(side=tk.LEFT, padx=2)

medium_button = tk.Button(size_frame, text="Medium", command=set_medium_pen)
medium_button.pack(side=tk.LEFT, padx=2)

large_button = tk.Button(size_frame, text="Large", command=set_large_pen)
large_button.pack(side=tk.LEFT, padx=2)

canvas = tk.Canvas(window, bg="white")
canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# bind mouse events to the canvas

# This records the starting coordinates for drawing
canvas.bind("<Button-1>", start_position)
canvas.bind("<B1-Motion>", draw_line)  # This tracks movement and draws lines

instruction_label = tk.Label(
    window, text="Click and drag to draw", font=("Arial", 12))
instruction_label.pack(pady=5)

# Calling The Loop

window.mainloop()
