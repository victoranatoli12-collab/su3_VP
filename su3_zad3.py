
class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        super().print()
        print("Университет:", self.university)
        print("Преподавателски стаж:", self.experience, "години")


l1 = Lecturer("Георги", "Стоянов", 45, "Българин", "ТУ София", 20)
l2 = Lecturer("Елена", "Иванова", 38, "Българка", "СУ", 12)

l1.print()
print()
l2.print()
