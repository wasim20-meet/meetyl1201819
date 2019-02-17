import startButtons
from startButtons import *
import random

def Skeleton1():
	Skeleton = turtle.clone() 
	Skeleton.showturtle()
	Skeleton.shape("SkeletonStanding.gif")
	Skeleton.goto(random.randint(-260,260),-100)


s = turtle.getscreen()
def moveRight():
	Princess.goto(Princess.pos()[0]+Princess.movement,Princess.pos()[1])
	Princess.shape("CharacterRight.gif")
def moveLeft():
	Princess.goto(Princess.pos()[0]-Princess.movement,Princess.pos()[1])
	Princess.shape("CharacterLeft.gif")
def moveUp():
	Princess.goto(Princess.pos()[0],Princess.pos()[1]+Princess.movement)
def moveDown():
	Princess.goto(Princess.pos()[0],Princess.pos()[1]-Princess.movement)
def pos():
	print(Princess.pos())


def movement():
	s.onkey(pos, "p")
	s.onkey(moveLeft, 'a')
	Princess.pencolor('red')
	s.onkey(moveRight, 'd')
	Princess.pencolor('red')
	s.onkey(moveUp, 'w')
	Princess.pencolor('red')
	s.onkey(moveDown, 's')
	Princess.pencolor('red')
	s.onkey(F2, "f")
	turtle.listen()

def castleIn():
	if startButtons.BG == "castleIn.gif":
		if (Princess.pos()[0] + Princess.movement > 220):
			Princess.goto(Princess.pos()[0]-Princess.movement,Princess.pos()[1])
		if (Princess.pos()[0] - Princess.movement < -220):
			Princess.goto(Princess.pos()[0]+Princess.movement,Princess.pos()[1])
		if (Princess.pos()[1] + Princess.movement > 120):
			Princess.goto(Princess.pos()[0],Princess.pos()[1]-Princess.movement)
		if (Princess.pos()[1] - Princess.movement < -320):
			startButtons.BG = "CastleOut.gif"
			turtle.bgpic(startButtons.BG)
			Princess.goto(0,0)
			turtle.setup(560,450)
			Skeleton1()
		

def castleOut():
	yListRightCastle = []
	xListDownRightCastle = []
	xListDownLeftCastle = []
	yListLeftCastle = []
	if startButtons.BG == "CastleOut.gif":
		for y in range(0,241):
			for x in range(155,165):
				yListRightCastle.append((x,y))
		for x in range(20,171):
			for y in range(0,10):
				xListDownRightCastle.append((x,y))
		for x in range(-200,20):
			for y in range(0,10):
				xListDownLeftCastle.append((x,y))
		for y in range(0,221):
			for x in range(-200,-190):
				yListLeftCastle.append(((x,y)))
		if Princess.pos() in yListRightCastle:
			Princess.goto(Princess.pos()[0]+Princess.movement,Princess.pos()[1])
		if Princess.pos() in yListLeftCastle:
			Princess.goto(Princess.pos()[0]-Princess.movement,Princess.pos()[1])
		if Princess.pos() in xListDownLeftCastle:
			Princess.goto(Princess.pos()[0],Princess.pos()[1]-Princess.movement)
		if Princess.pos() in xListDownRightCastle:
			Princess.goto(Princess.pos()[0],Princess.pos()[1]-Princess.movement)
		if Princess.pos()[0] + Princess.movement > 280:
			startButtons.BG = "Yard.gif"
			turtle.bgpic(startButtons.BG)
			Princess.goto(-280 + Princess.movement ,Princess.pos()[1])
		if Princess.pos()[0] - Princess.movement < -280:
			startButtons.BG = "Yard.gif"
			turtle.bgpic(startButtons.BG)
			Princess.goto(280 - Princess.movement ,Princess.pos()[1])