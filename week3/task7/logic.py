def calculate_square(text):
    try:
        num = float(text)
        return f"Результат: {num ** 2}"
    except ValueError:
        return "Введіть число!"