import math
class Shape:
    def __init__(self, border_color, border_thickness, location):
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.location = location

    def __str__(self):
        return f"{self.__class__.__name__} the attributes are as follows:\nColor ->{self.border_color}\nThickness -> {self.border_thickness}\nLocation -> {self.location}"
    
    def change_border_color(self, color):
        self.border_color = color

    def change_border_thickness(self, thickness):
        self.border_thickness = thickness


class Circle(Shape):
    def __init__(self,radius,border_color, border_thickness, location):
        super().__init__(border_color, border_thickness, location)
        self.radius = radius

    def __str__(self):
        return f"The circle features are as follows : \nRadius -> {self.radius}\nColor -> {self.border_color}\nThickness -> {self.border_thickness}\nLocation -> {self.location}"
    
    def Area(self):
        return f"The area of the circle is {math.pi * self.radius ** 2} cm²"

