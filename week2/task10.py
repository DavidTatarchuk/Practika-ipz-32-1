class Car:
    def __init__(self, make, year, mileage):
        self.make = make
        self.year = year
        self._mileage = mileage

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value < 0:
            print(f"Помилка: Пробіг ({value}) не може бути від'ємним!")
        else:
            self._mileage = value

    def __str__(self):
        return f"{self.make}: пробіг {self._mileage} км"

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            print("Помилка: Ширина повинна бути додатною!")
        else:
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            print("Помилка: Висота повинна бути додатною!")
        else:
            self._height = value

    def area(self):
        return self._width * self._height

car = Car("BMW X5", 2022, 15000)
print(car)

car.mileage = -500
car.mileage = 20000
print(car)

print("-" * 30)

rect = Rectangle(10, 5)
print(f"Площа: {rect.area()}")

rect.width = -10
rect.width = 20
print(f"Нова площа: {rect.area()}")