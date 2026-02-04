def factorial(n):
    # Базовый случай: факториал 0 и 1 равен 1
    if n == 0 or n == 1:
        return 1
    # Рекурсивный шаг: число умножаем на факториал (число - 1)
    return n * factorial(n - 1)

# Ввод числа
number = int(input("Введіть ціле число: "))

# Вызов функции и вывод результата
result = factorial(number)
print(f"Факторіал {number}! = {result}")