import tkinter as tk
from tkinter import messagebox

def get_button(window, text, color, command, fg='White'):
    button = tk.Button(
        window,
        text=text,
        activebackground='black',
        activeforeground='white',
        fg=fg,
        bg=color,
        command=command,
        height=2,
        width=20,
        font=('Helvetica bold', 20)
    )
    return button

def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label

def get_text_label():
    label = tk.Label(window, text=text)
    label.config(font=("sans-serif", 21), justify='left')
    return label

