import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    path = filedialog.askopenfilename()
    if path:
        with open(path, "r", encoding="utf-8") as f:
            text.delete("1.0", tk.END)
            text.insert("1.0", f.read())
        text.edit_modified(False)

def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))
        text.edit_modified(False)

def exit_app():
    if text.edit_modified():
        if not messagebox.askyesno("Увага", "Є незбережені зміни. Вийти?"):
            return
    root.destroy()

root = tk.Tk()
root.title("Блокнот")

text = tk.Text(root)
text.pack(expand=True, fill="both")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Файл", menu=file_menu)

file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_command(label="Вийти", command=exit_app)

root.protocol("WM_DELETE_WINDOW", exit_app)
root.mainloop()