class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point ({self.x} , {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x , self.y + other.y)
    
p1 = Point(2,3)
p2 = Point(4,5)

print(p1,"\n",p2)
print(f"Point1 + Point2 -> {p1 + p2}")