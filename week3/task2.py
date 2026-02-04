import tkinter as tk

def greet():
    label.config(text="Вітаю, користувач!")

def clear():
    label.config(text="")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Завдання 2")
root.geometry("400x300")

label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=50)

btn_greet = tk.Button(root, text="Привітати", command=greet, width=15)
btn_greet.pack(pady=5)

btn_clear = tk.Button(root, text="Очистити", command=clear, width=15)
btn_clear.pack(pady=5)

btn_exit = tk.Button(root, text="Вийти", command=exit_app, width=15)
btn_exit.pack(pady=5)

root.mainloop()