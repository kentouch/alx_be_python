### define a base class called "Shape", with a method area that raise an error "NotImplementError"
# We will define also derived classes as rectangle and circle that will overide this area method


import math
class Shape:
    def area(self): 
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)