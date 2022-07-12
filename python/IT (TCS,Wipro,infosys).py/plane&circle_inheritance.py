import math

class Plane:
    def __init__(self,x1,y1):
        self.x1=x1
        self.y1=y1
    def show(self):
        print(f"The first coordinate is= ({self.x1} , {self.y1})")

class Circle(Plane):
    def __init__(self,x1,y1,x2,y2):
        self.x2=x2
        self.y2=y2
        Plane.__init__(self,x1,y1)
        
    def findradius(self):
        self.r=(math.sqrt(self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)/2
    
    def findarea(self):
        self.A=(math.pi*self.r*self.r)

    def show(self):
        print(f"Length of the radius is '{self.r}' and Are of the circle is '{self.A}'")

obj1=Plane(34,67)
print()
obj1.show()
print()
obj2=Circle(4,6,5,8)
obj2.findradius()
obj2.findarea()
obj2.show()
print() 