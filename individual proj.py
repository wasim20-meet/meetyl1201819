import turtle
from turtle import Turtle
class Ball (Turtle):
	def __init__ (self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.penup()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)

b1 = Ball(5,25,15,15,200,"red")

turtle.mainloop()

