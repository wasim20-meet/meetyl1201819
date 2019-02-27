#the circle class for the 3 in a row game
from turtle import Turtle 
import turtle
import random
listcol=["sky blue","hot pink","tan","gold"]
class Circle(Turtle):
	"""A turtle that is showing in the screen as a turtle """
	def __init__(self,row,col):
		Turtle.__init__(self)
		self.penup()
		self.row=row
		self.col=col
		self.goto(-455+(90*row),360-(90*col))
		self.shape("turtle")
		self.shapesize(2.3)
		self.left(90)
		color=(random.choice(listcol))
		self.fillcolor(color)
		self.color(color)
		self.color1=color


		


