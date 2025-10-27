class Shape:
    def __init__(self, sides, x, y):
        self.sides = sides
        self.x = x
        self.y = y

    def perimeter(self):
        pass

    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, x, y, side_length):
        self.s1 = side_length
        self.s2 = side_length
        self.s3 = side_length
        super().__init__(3, x, y)
    
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
    
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        super().__init__(4, x, y)
    
    def perimeter(self):
        return 2 * self.width + 2 * self.height

t = Triangle(50, 50, 6)
print(t.perimeter())
r = Rectangle(20, 20, 10, 10)
print(r.perimeter())