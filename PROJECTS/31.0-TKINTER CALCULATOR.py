import tkinter as tk


def calculate_sum():
    try:
        num1 = float(first_number.get())
        num2 = float(second_number.get())

        result = num1 + num2

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


def calculate_sub():
    try:
        num3 = float(first_number.get())
        num4 = float(second_number.get())

        result1 = num3 - num4

        result_label.config(text=f"Result: {result1}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


def calculate_multi():
    try:
        num5 = float(first_number.get())
        num6 = float(second_number.get())

        result2 = num5 * num6

        result_label.config(text=f"Result: {result2}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


def calculate_division():
    try:
        num7 = float(first_number.get())
        num8 = float(second_number.get())

        result3 = num7 / num8

        result_label.config(text=f"Result: {result3}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

# Main window


window = tk.Tk()
window.title("Simple Tkinter Calculator App")
window.geometry("1000x430")

title_label = tk.Label(
    window, text="Simple Calculator", font=("Arial", 20))
title_label.pack(pady=20)

frame1 = tk.Frame(window)
frame1.pack(pady=5)

num1_label = tk.Label(frame1, text="First Number: ")
num1_label.pack(side=tk.LEFT)

first_number = tk.Entry(frame1, width=10)
first_number.pack()

frame2 = tk.Frame(window)
frame2.pack(pady=5)

num2_label = tk.Label(frame2, text="Second Number: ")
num2_label.pack(side=tk.LEFT)

second_number = tk.Entry(frame2, width=10)
second_number.pack()

calculate_button1 = tk.Button(
    window, text="Add Numbers", command=calculate_sum)
calculate_button1.pack(pady=10)

calculate_button2 = tk.Button(
    window, text="Subtract Numbers", command=calculate_sub)
calculate_button2.pack(pady=10)

calculate_button3 = tk.Button(
    window, text="Multiple Numbers", command=calculate_multi)
calculate_button3.pack(pady=10)

calculate_button4 = tk.Button(
    window, text="Divide numbers", command=calculate_division)
calculate_button4.pack(pady=10)

result_label = tk.Label(window, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)


def clear_fields():
    first_number.delete(0, tk.END)
    second_number.delete(0, tk.END)
    result_label.config(text="Result: ")


clear_button = tk.Button(window, text="Clear", command=clear_fields)
clear_button.pack(pady=5)

window.mainloop()
