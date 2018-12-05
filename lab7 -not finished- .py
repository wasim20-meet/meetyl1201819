from turtle import *
import random
import turtle
import math
class Ball(Turtle):
	def __init__ (self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		self.penup()
def check_collision(ball1,ball2):
	p1 = ball1.position()
	p2 = ball2.position()
	distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
	if ((ball2.radius > distance) or (ball1.radius > distance)):
		return True
	return False

b1 = Ball(50, 'blue', 100)
b2 = Ball(20, 'red', 100)
print(check_collision(b1,b2))
turtle.mainloop()
ls = [b1,b2]
if (ls[1].radius >= ls[0].radius):
	ls[1].goto(random.randint())