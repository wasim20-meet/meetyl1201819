import turtle
from turtle import Turtle
import random
turtle.colormode(255)
class Rectangle(Turtle):
	def __init__ (self,x,y):
		Turtle.__init__(self)
		turtle.register_shape("rectangle",((0,0),(0,y),(x,y),(x,0),(0,0)))
		self.shape("rectangle")

# rect = Rectangle(75,100)
class Square(Rectangle):
	def __init__ (self):
		Rectangle.__init__(self,50,50)
	def random_color(self):
		r = random.randint(0,255)
		r1 = random.randint(0,255)
		r2 = random.randint(0,255)
		self.color([r,r1,r2])
# Square = Square()
# Square.random_color()

# class Hexagon(Turtle):
# 	def 


turtle.mainloop()