class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Гав-гав")

class Cat(Animal):
    def sound(self):
        print("Мяу")

class Cow(Animal):
    def sound(self):
        print("Му-у")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()