import tkinter as tk

def save_data():
    name = entry_name.get()
    gender = gender_var.get()
    agreement = "Так" if agree_var.get() else "Ні"
    
    result_text = f"Ім'я: {name}\nСтать: {gender}\nЗгода: {agreement}"
    label_result.config(text=result_text)

root = tk.Tk()
root.title("Анкета користувача")
root.geometry("300x300")

tk.Label(root, text="Ваше ім'я:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Стать:").grid(row=1, column=0, padx=10, pady=5, sticky="w")

gender_var = tk.StringVar(value="Чоловіча")
tk.Radiobutton(root, text="Чоловіча", variable=gender_var,
         value="Чоловіча").grid(row=1, column=1, sticky="w")

tk.Radiobutton(root, text="Жіноча", variable=gender_var, 
      value="Жіноча").grid(row=2, column=1, sticky="w")

agree_var = tk.BooleanVar()
tk.Checkbutton(root, text="Погоджуюсь із умовами",
      variable=agree_var).grid(row=3, column=0, columnspan=2, pady=10)

tk.Button(root, text="Зберегти", command=save_data).grid(row=4,
     column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="", fg="blue", justify="left")
label_result.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()