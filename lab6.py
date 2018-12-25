from turtle import Turtle
import random
import turtle 
turtle.speed(100)
turtle.tracer(0)
# turtle.colormode(255)
# class Rectangle(Turtle):
# 	def __init__ (self,x,y):
# 		Turtle.__init__(self)
# 		turtle.register_shape("rectangle",((0,0),(0,y),(x,y),(x,0),(0,0)))
# 		self.shape("rectangle")
# 	def random_color(self):
# 		r = random.randint(0,255)
# 		r1 = random.randint(0,255)
# 		r2 = random.randint(0,255)
# 		self.color([r,r1,r2])


# rect = Rectangle(75,100)
# rect.random_color();
# class Square(Rectangle):
# 	def __init__ (self):
# 		Rectangle.__init__(self,50,50)
	
# Square = Square()
# Square.random_color()

# class Hexagon(Turtle):
# 	def __init__(self, x):
# 		Turtle.__init__(self)
# 		turtle.register_shape("Hexagon",((0,0),(x,0),(2*x,x),(2*x,2*x),(x,3*x),(0,3*x),(-x,2*x),(-x,x),(0,0)))
# 		self.shape("Hexagon")
# 	def random_color(self):
# 		r = random.randint(0,255)
# 		r1 = random.randint(0,255)
# 		r2 = random.randint(0,255)
# 		self.color([r,r1,r2])

# H = Hexagon(20)
# H.random_color()


## vvv not working vvv

# class Polygon(Turtle):
# 	def __init__(self,x,length):
# 		Turtle.__init__(self)
# 		angle = 180*(x-2)
# 		angle1 = angle / x
# 		turtle.begin_fill()
# 		turtle.begin_poly()
# 		for y in range(x):
# 			turtle.right(angle1)
# 			turtle.forward(length)
# 		turtle.end_fill()
# 		turtle.end_poly()
# 		sh = turtle.get_poly()
# 		turtle.register_shape("Poly1",sh)
# 		self.shape("Poly1")
# d = Polygon(8,50)
# turtle.mainloop()