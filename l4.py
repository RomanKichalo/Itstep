import math

class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle("red", 5)
print(f"Circle color: {circle.color}, area: {circle.area()}")


rectangle = Rectangle("green", 4, 6)
print(f"Rectangle color: {rectangle.color}, area: {rectangle.area()}")
