import tkinter as tk
import logic

class MainWindow:
    def __init__(self, root):
        root.title("Модульна програма")
        root.geometry("300x200")

        self.entry = tk.Entry(root)
        self.entry.pack(pady=20)

        self.btn = tk.Button(root, text="Піднести до квадрату", command=self.on_click)
        self.btn.pack()

        self.label = tk.Label(root, text="")
        self.label.pack(pady=20)

    def on_click(self):
        # Отримуємо дані з поля
        data = self.entry.get()
        # Відправляємо в логіку
        result = logic.calculate_square(data)
        # Показуємо результат
        self.label.config(text=result)