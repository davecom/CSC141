#!/usr/bin/env python3

import turtle

def teleport(x, y):
	turtle.setx(x)
	turtle.sety(y)

class Shape:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.stroke_width = 1
		self.color = "black"
		
	@property
	def area(self):
		pass
	
	@property
	def perimeter(self):
		pass
		
	def draw(self):
		turtle.width(self.stroke_width)
		turtle.color(self.color)
		
	def set_stroke_width(self, w):
		self.stroke_width = w
	
	def set_color(self, c):
		self.color = c
		
class Circle(Shape):
	def __init__(self, x, y, radius):
		super().__init__(x, y)
		self.radius = radius
	
	@property
	def area(self):
		return pi * self.radius * self.radius
	
	@property
	def perimeter(self):
		return self.radius * 2 * pi
	
	def draw(self):
		super().draw()
		teleport(self.x + self.radius, self.y)
		turtle.setheading(90)
		turtle.circle(self.radius)
	
class Rectangle(Shape):
	def __init__(self, x, y, width, height):
		super().__init__(x, y)
		self.width = width
		self.height = height	
	
	@property
	def area(self):
		return self.width * self.height
	
	@property
	def perimeter(self):
		return 2 * self.width + 2 * self.height
	
	def move(self, dx, dy):
		self.x += dx
		self.y += dy
		
	def draw(self):
		super().draw()
		tlx = self.x - (self.width / 2)
		tly = self.y - (self.height / 2)
		teleport(tlx, tly)
		turtle.forward(self.width)
		turtle.right(90)
		turtle.forward(self.height)
		turtle.right(90)
		turtle.forward(self.width)
		turtle.right(90)
		turtle.forward(self.height)
		
		
class Square(Rectangle):
	def __init__(self, x, y, side_length):
		super().__init__(x, y, side_length, side_length)
		
class Line(Shape):
	def __init__(self, x1, y1, x2, y2):
		super().__init__(((x1 + x2) / 2), ((y1 + y2) / 2))
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2

	
	def draw(self):
		super().draw()
		teleport(self.x1, self.y1)
		turtle.goto(self.x2, self.y2)

class Triangle(Shape):
	def __init__(self, x1, y1, x2, y2, x3, y3):
		super().__init__(((x1 + x2 + x3) / 3), ((y1 + y2 + y3) / 3))
		self.x1 = x1
		self.x2 = x2
		self.x3 = x3
		self.y1 = y1
		self.y2 = y2
		self.y3 = y3
		
	def draw(self):
		super().draw()
		l1 = Line(self.x1, self.y1, self.x2, self.y2)
		l1.draw()
		l2 = Line(self.x2, self.y2, self.x3, self.y3)
		l2.draw()
		l3 = Line(self.x3, self.y3, self.x1, self.y1)
		l3.draw()
c = Circle(70, 70, 40)
c.draw()
r = Rectangle(100, 100, 100, 70)
print(r.perimeter)
r.draw()
#s = Square(200, 180, 40)
#c = Circle(200, 180, 20)
#c.set_color("blue")
#l = Line(100, 20, 20, 100)
#l.set_stroke_width(10)
#t = Triangle(0, 0, 150, 150, 300, 0)
#
#def cutPaper(shape):
#	pass
#	
#class Pentagon:
#	def perimeter(self):
#		pass
#	def area(self):
#		pass
#	def draw(self):
#		pass
#
#
#cutPaper(Square(<#x#>, <#y#>, <#side_length#>))
#cutPaper(Circle(<#x#>, <#y#>, <#radius#>))
#cutPaper(Pentagon())
#
#shapes = [r, s, c, l, t]
#for shape in shapes:
#	shape.draw()
#
## pause
#input()