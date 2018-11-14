import turtle
from turtle import Turtle
import random
turtle.colormode(255)
class Square(Turtle):
	def __init__ (self, size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)
	def random_color(self):
		r = random.randint(0,255)
		r1 = random.randint(0,255)
		r2 = random.randint(0,255)
		self.color([r,r1,r2])
s = Square(8)
s.random_color()
Square = Square(3)
Square.random_color()
turtle.mainloop()