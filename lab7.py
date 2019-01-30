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


b1 = Ball(50, 'blue', 10)
b2 = Ball(20, 'red', 15)
ballslist = [b1,b2]
while(check_collision(b1,b2) == True):
	if(ballslist[0].radius < ballslist[1].radius):
		ballslist[0].goto((random.randint(1,450)),(random.randint(1,450)))
	else:
		ballslist[1].goto((random.randint(1,450)),(random.randint(1,450)))

turtle.mainloop()