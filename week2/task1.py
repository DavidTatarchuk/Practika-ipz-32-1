import math

def area_rectangle_proc(width, height):
    return width * height

def area_circle_proc(radius):
    return math.pi * (radius ** 2)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

print("--- Процедурний підхід ---")
print(f"Прямокутник: {area_rectangle_proc(10, 5)}")
print(f"Коло: {area_circle_proc(5):.2f}")

print("\n--- Об'єктно-орієнтований підхід ---")
rect = Rectangle(10, 5)
circle = Circle(5)
print(f"Прямокутник: {rect.area()}")
print(f"Коло: {circle.area():.2f}")