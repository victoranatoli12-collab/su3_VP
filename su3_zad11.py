
class EBook(Book):
    def __init__(self, title, author, year, format, size):
        super().__init__(title, author, year)
        self.format = format
        self.size = size

    def print(self):
        super().print()
        print("Формат:", self.format)
        print("Размер:", self.size, "MB")


ebook1 = EBook("Под игото", "Иван Вазов", 1894, "PDF", 5)
ebook2 = EBook("Тютюн", "Димитър Димов", 1951, "EPUB", 3)

ebook1.print()
print()
ebook2.print()
