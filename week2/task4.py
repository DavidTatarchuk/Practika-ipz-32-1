class Car:
    def __init__(self, make, year, mileage):
        self.make = make
        self.year = year
        self.mileage = mileage

    def drive(self, km):
        if km > 0:
            self.mileage += km

    def info(self):
        print(f"Марка: {self.make}, Рік: {self.year}, Пробіг: {self.mileage} км")

    def __str__(self):
        return f"{self.make} ({self.year}) — {self.mileage} км"

car1 = Car("Toyota Camry", 2019, 45000)
car2