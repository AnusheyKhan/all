import math


class Circle:

    def __init__(self):
        self.radius = 0



    def area(self):
        return math.pi * self.radius * self.radius


class Cylinder(Circle):

    def __init__(self):
        super().__init__()
        self.height = 0


    def surfaceArea(self):
        result = 2 * math.pi * getattr(self, "radius") * self.height + 2 * super().area()
        return result

    def Volume(self):
        result = super().area() * self.height
        return result


obj = Cylinder()
print("The surface area is " + str(obj.surfaceArea()))
print("The Volume is " + str(obj.Volume()))


class Cylinder2:

    def __init__(self):
        self.circle = Circle()
        self.height = 0

    def surfaceArea(self):
        result = 2 * math.pi * getattr(self.circle, "radius") * self.height + 2 * self.circle.area()
        return result

    def Volume(self):
        result = self.circle.area() * self.height
        return result

obj = Cylinder2()
print("The surface area is " + str(obj.surfaceArea()))
print("The Volume is " + str(obj.Volume()))
