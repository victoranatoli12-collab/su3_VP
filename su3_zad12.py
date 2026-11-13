
import math


class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


r = Rectangle(5, 3)
c = Circle(4)

print("Лице на правоъгълника:", r.area())
print("Лице на кръга:", c.area())
