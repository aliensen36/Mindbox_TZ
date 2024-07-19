import math

class Shape:
    def area(self):
        raise NotImplementedError("Это метод должен быть переопределен.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def is_right_angle(self):
        sides = sorted([self.side1, self.side2, self.side3])
        return math.isclose(sides[2]**2, sides[0]**2 + sides[1]**2)

def calculate_area(shape: Shape):
    return shape.area()

# Пример добавления новых фигур
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
