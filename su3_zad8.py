
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_capacity):
        super().__init__(brand, model, year)
        self.engine_capacity = engine_capacity

    def print(self):
        super().print()
        print("Кубатура:", self.engine_capacity, "куб.см")


m1 = Motorcycle("Honda", "CBR", 2021, 600)
m2 = Motorcycle("Yamaha", "R1", 2022, 1000)

m1.print()
print()
m2.print()
