#distance is a class. Distance is measured in terms of feet and inches
class distance:
    def __init__(self, f, i):
        self.feet = f 
        self.inches = i

#overloading of binary operator > to compare two distances 
    def __gt__(self, d):
        if self.feet > d.feet:
            return True
        elif self.feet == d.feet and self.inches > d.inches: 
            return True
        else: 
            return False
        
#overloading of binary operator + to add two distances 
    def __add__(self, d):
        i = self.inches + d.inches 
        f = self.feet + d.feet 
        if i >= 12:
            i -= 12
            f += 1
            return distance(f, i)
        
# displaying the distance 
    def show(self):
        print("Feet =", self.feet, "Inches =", self.inches)
        
a, b = map(int, input("Enter feet and inches of distance1: ").split()) 
c, d = map(int, input("Enter feet and inches of distance2: ").split()) 
d1 = distance(a, b) 
d2 = distance(c, d)

if d1 > d2: 
    print("Distance1 is greater than Distance2") 
else:
    print("Distance2 is greater or equal to Distance1") 
        
d3 = d1+d2 
print("Sum of the two Distance is:") 
d3.show()
