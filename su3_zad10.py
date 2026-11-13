
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def print(self):
        print("Заглавие:", self.title)
        print("Автор:", self.author)
        print("Година:", self.year)


b1 = Book("Под игото", "Иван Вазов", 1894)
b2 = Book("Бай Ганьо", "Алеко Константинов", 1895)
b3 = Book("Тютюн", "Димитър Димов", 1951)

b1.print()
print()
b2.print()
print()
b3.print()
