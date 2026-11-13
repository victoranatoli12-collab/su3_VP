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


class Manager(Employee):
    def __init__(self, name, position, salary, department):
        super().__init__(name, position, salary)
        self.department = department

    def print(self):
        super().print()
        print("Отдел:", self.department)


    m1 = Manager("Иван", "Мениджър", 4000, "IT")
    m2 = Manager("Мария", "Мениджър", 3500, "Продажби")

    e1.print()
    print()
    e2.print()
    print()
    e3.print()

    m1.print()
    print()
    m2.print()
