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
	def move(self,screen_width,screen_height):
		Up_edge = screen_height
		Right_edge = screen_width
		Down_edge = screen_height * -1
		Left_edge = screen_width * -1
		
		current_x = self.xcor()
		current_y = self.ycor()
		new_x = current_x + self.dx
		new_y = current_y + self.dy
		right_side = self.r + new_x
		left_side =  new_x - self.r
		up_side = self.r + new_y
		down_side =  new_y - self.r
		if ((right_side > Right_edge) or (left_side < Left_edge)):
			self.dx = self.dx * -1
		if ((up_side > Up_edge) or (down_side < Down_edge)):
			self.dy = self.dy * -1
		self.goto(new_x,new_y)
