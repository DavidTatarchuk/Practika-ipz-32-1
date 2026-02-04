a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

D = b**2 - 4*a*c
print("Дискримінант =", D)

if D > 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print("x1 =", x1)
    print("x2 =", x2)
elif D == 0:
    x = -b / (2 * a)
    print("Єдиний корінь x =", x)
else:
    print("Дійсних коренів немає")