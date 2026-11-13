
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print("Животното издава звук")


class Dog(Animal):
    def sound(self):
        print(self.name, "казва: Бау!")


class Cat(Animal):
    def sound(self):
        print(self.name, "казва: Мяу!")


dog = Dog("Шаро", 3)
cat = Cat("Мая", 2)

dog.sound()
cat.sound()
