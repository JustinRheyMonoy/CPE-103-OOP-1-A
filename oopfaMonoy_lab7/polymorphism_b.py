class RegularPolygon:
    def __init__ (self, side):
        self._side = side

class Square (RegularPolygon):
    def area (self):
        return self._side * self._side

class EquilateralTriangle (RegularPolygon):
    def area (self):
        return self._side * self._side * 0.433
    
obj1 = Square(4)
obj2 = EquilateralTriangle(3)

print(obj1.area())
print(obj2.area())