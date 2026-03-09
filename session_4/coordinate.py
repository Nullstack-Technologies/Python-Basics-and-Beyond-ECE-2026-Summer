import math

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
    
    def midpoint(self, p):
        return Point((self.x + p.x) / 2, (self.y + p.y)  / 2)
        
p1 = Point(3, 2)
p2 = Point(2, 3)

print(p1.distance(p2))
print(p2.distance(p1))