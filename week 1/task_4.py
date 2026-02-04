import math

v0 = float(input("Введіть початкову швидкість (м/с): "))
angle = float(input("Введіть кут вильоту (градуси): "))

g = 9.81
rad = math.radians(angle)

total_time = (2 * v0 * math.sin(rad)) / g
max_height = (v0**2 * (math.sin(rad)**2)) / (2 * g)
distance = v0 * math.cos(rad) * total_time

print("-" * 30)
print(f"Дальність польоту: {distance:.2f} м")
print(f"Максимальна висота: {max_height:.2f} м")
print(f"Загальний час: {total_time:.2f} с")
print("-" * 30)

print("Висота по секундах:")
t = 0
while t < total_time:
    h = v0 * t * math.sin(rad) - (0.5 * g * t**2)
    print(f"Час {t} с: висота {h:.2f} м")
    t += 1