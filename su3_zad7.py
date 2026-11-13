
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
