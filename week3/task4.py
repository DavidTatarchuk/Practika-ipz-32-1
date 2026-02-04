import tkinter as tk

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = 0

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                label_result.config(text="Помилка: ділення на 0", fg="red")
                return
            result = num1 / num2
        
        label_result.config(text=f"Результат: {result}", fg="black")

    except ValueError:
        label_result.config(text="Помилка: введіть числа", fg="red")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x250")

tk.Label(root, text="Число 1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Число 2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="+", width=5, command=lambda: calculate("+")).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="-", width=5, command=lambda: calculate("-")).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="*", width=5, command=lambda: calculate("*")).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="/", width=5, command=lambda: calculate("/")).grid(row=0, column=3, padx=5)

label_result = tk.Label(root, text="Результат:", font=("Arial", 12, "bold"))
label_result.pack(pady=20)

root.mainloop()