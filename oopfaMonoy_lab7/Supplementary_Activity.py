import math

class RegularPolygon:
    def __init__(self, side):
        self._side = side

class Square(RegularPolygon):
    def area(self):
        return self._side * self._side

class EquilateralTriangle(RegularPolygon):
    def area(self):
        return self._side * self._side * 0.433

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Pentagon(RegularPolygon):
    def area(self):
        return (5 * self._side * self._side) / (4 * math.tan(math.pi / 5))

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius * self.radius

# Creating objects for each shape
obj1 = Square(4)
obj2 = EquilateralTriangle(3)
obj3 = Rectangle(5, 3)
obj4 = Pentagon(4)
obj5 = Circle(3)

# Displaying areas of each shape
print("Square Area:", obj1.area())
print("Equilateral Triangle Area:", obj2.area())
print("Rectangle Area:", obj3.area())
print("Pentagon Area:", obj4.area())
print("Circle Area:", obj5.area())