import tkinter as tk
from tkinter import colorchooser, messagebox

# Глобальні змінні
current_color = "black"
current_tool = "line"
start_x, start_y = 0, 0
temp_shape = None  # Для збереження тимчасової фігури під час руху миші

def choose_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color

def set_tool(tool):
    global current_tool
    current_tool = tool

def on_press(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

def on_drag(event):
    global temp_shape
    # Видаляємо стару "примарну" фігуру, щоб намалювати нову в новій позиції
    if temp_shape:
        canvas.delete(temp_shape)
    
    if current_tool == "line":
        temp_shape = canvas.create_line(start_x, start_y, event.x, event.y, fill=current_color)
    else:
        temp_shape = canvas.create_oval(start_x, start_y, event.x, event.y, outline=current_color)

def on_release(event):
    global temp_shape
    temp_shape = None # Фіксуємо фігуру (просто перестаємо її видаляти)
    # Малюємо фінальну жирну фігуру
    if current_tool == "line":
        canvas.create_line(start_x, start_y, event.x, event.y, fill=current_color, width=2)
    else:
        canvas.create_oval(start_x, start_y, event.x, event.y, outline=current_color, width=2)

def clear_canvas():
    canvas.delete("all")

def save_image():
    try:
        canvas.postscript(file="drawing.ps", colormode="color")
        messagebox.showinfo("Успіх", "Збережено як drawing.ps")
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося зберегти: {e}")

root = tk.Tk()
root.title("Графіка")

# Панель інструментів
panel = tk.Frame(root)
panel.pack(fill="x")

tk.Button(panel, text="Лінія", command=lambda: set_tool("line")).pack(side="left", padx=5)
tk.Button(panel, text="Коло", command=lambda: set_tool("circle")).pack(side="left", padx=5)
tk.Button(panel, text="Колір", command=choose_color).pack(side="left", padx=5)
tk.Button(panel, text="Очистити", command=clear_canvas).pack(side="left", padx=5)
tk.Button(panel, text="Зберегти (.ps)", command=save_image).pack(side="right", padx=5)

# Полотно
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Прив'язка подій миші
canvas.bind("<Button-1>", on_press)       # Натискання
canvas.bind("<B1-Motion>", on_drag)       # Рух із затиснутою кнопкою
canvas.bind("<ButtonRelease-1>", on_release) # Відпускання

root.mainloop()