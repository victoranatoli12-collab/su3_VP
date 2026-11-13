
class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy

    def print(self):
        super().print()
        print("Университет:", self.university)
        print("Година на обучение:", self.yearofstudy)


s1 = Student("Петър", "Георгиев", 19, "Българин", "ТУ София", 1)
s2 = Student("Анна", "Димитрова", 20, "Българка", "СУ", 2)

s1.print()
print()
s2.print()
