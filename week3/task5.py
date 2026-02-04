import tkinter as tk
from tkinter import ttk, colorchooser
import os

CONFIG_FILE = "bg_color.txt"

def set_background(color):
    if color:
        tab1.config(bg=color)
        tab2.config(bg=color)
        tab3.config(bg=color)

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        set_background(color)
        with open(CONFIG_FILE, "w") as f:
            f.write(color)

def load_color():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            color = f.read().strip()
            set_background(color)

root = tk.Tk()
root.title("Багатовіконна програма")
root.geometry("400x300")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
tab3 = tk.Frame(notebook)

notebook.add(tab1, text="Головна")
notebook.add(tab2, text="Налаштування")
notebook.add(tab3, text="Про програму")

tk.Label(tab1, text="Введіть ваше ім'я:").pack(pady=10)
tk.Entry(tab1).pack(pady=5)
tk.Button(tab1, text="Підтвердити").pack(pady=20)

tk.Button(tab2, text="Вибрати колір фону", command=choose_color).pack(expand=True)

tk.Label(tab3, text="Автор: Студент курсу\nРік: 2026", font=("Arial", 12)).pack(expand=True)

load_color()

root.mainloop()