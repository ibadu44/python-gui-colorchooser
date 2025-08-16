import tkinter as tk
from tkinter import colorchooser

def pick_color():
    color = colorchooser.askcolor()[1]  # Get hex color
    if color:
        root.config(bg=color)
        label.config(text=f"Selected: {color}", bg=color)

root = tk.Tk()
root.title("Color Picker")
root.geometry("300x200")

btn = tk.Button(root, text="Pick a Color", command=pick_color, font=("Arial", 14))
btn.pack(pady=20)

label = tk.Label(root, text="No color chosen", font=("Arial", 12))
label.pack()

root.mainloop()
