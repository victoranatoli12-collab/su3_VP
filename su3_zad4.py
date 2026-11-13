
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def print(self):
        print("Име:", self.name)
        print("Длъжност:", self.position)
        print("Заплата:", self.salary, "лв.")


e1 = Employee("Иван", "Програмист", 2500)
e2 = Employee("Мария", "Счетоводител", 2000)
e3 = Employee("Петър", "Техник", 1800)

e1.print()
print()
e2.print()
print()
e3.print()
 