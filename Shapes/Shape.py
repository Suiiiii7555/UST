from abc import ABC, abstractmethod
import math

class shapes(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        # raise NotImplementedError(f"area method is not defined for {self.__class__.__name__}")
        pass

    def get_color(self):
        return self.color
    

class Circle(shapes):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return f"Area of circle is : {math.pi * (self.radius ** 2)} cm²"


class Rectangle(shapes):
    def __init__(self, color,length, breadth):
        super().__init__(color)
        self.color = color
        self.breadth = breadth
        self.length = length

    def area(self):
        return f"Area of rectangle is : {self.length * self.breadth} cm²"


c1 = Circle("red",10)
r1 = Rectangle("blue", 10, 8)

print(f"Area of circle {c1.area()}")
print(f"Area of rectangle {r1.area()}")