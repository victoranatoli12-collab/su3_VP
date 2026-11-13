
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print(self):
        print("Марка:", self.brand)
        print("Модел:", self.model)
        print("Година:", self.year)


v1 = Vehicle("BMW", "X5", 2020)
v2 = Vehicle("Audi", "A4", 2019)
v3 = Vehicle("Toyota", "Corolla", 2022)

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def print(self):
        super().print()
        print("Брой врати:", self.doors)


c1 = Car("BMW", "i4", 2020, 5)
c2 = Car("Audi", "A3", 2019, 4)

c1.print()
print()
c2.print()
