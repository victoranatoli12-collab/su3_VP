
class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print("Име:", self.name)
        print("Фамилия:", self.family)
        print("Възраст:", self.age)
        print("Националност:", self.nationality)


p1 = Person("Иван", "Иванов", 20, "Българин")
p2 = Person("Мария", "Петрова", 21, "Българка")

p1.print()
print()
p2.print()
