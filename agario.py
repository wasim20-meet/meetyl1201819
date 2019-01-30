import turtle 
import ball
import random
from ball import Ball
import math
import time
import string
import Tkinter as tk
import tkSimpleDialog as simpledialog
colmb = simpledialog.askstring("Input", "Enter Color", parent=tk.Tk().withdraw())
radmb = int(simpledialog.askstring("Input", "Enter radius between 10 and 50", parent=tk.Tk().withdraw()))
while (radmb > 50 or radmb <10):
	if ((radmb > 50) or (radmb < 10)):
		radmb = int(simpledialog.askstring("Input", "Enter radius between 10 and 50", parent=tk.Tk().withdraw()))

RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
turtle.tracer(0,0)
MY_BALL = Ball(0,0,0,0,radmb,colmb,colmb)
score = turtle.clone()
score.hideturtle()
pos = score.pos()
turtle.hideturtle()
turtle.bgcolor("black")
turtle.pencolor("white")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 20
MAXIMUM_BALL_RADIUS = 60
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = []
NUMBER_OF_DOTS = 20
RADIUS_OF_DOTS = 10
DOTS = []
score.penup()


for n in range(NUMBER_OF_BALLS):
	x = random.randint((-SCREEN_WIDTH + 20) + MAXIMUM_BALL_RADIUS, (SCREEN_WIDTH - 20) - MAXIMUM_BALL_RADIUS)
	y = random.randint((-SCREEN_HEIGHT + 20) + MAXIMUM_BALL_RADIUS, (SCREEN_HEIGHT -20)- MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	new_ball = Ball(x,y,dx,dy,radius,color,color)

	BALLS.append(new_ball)


for dot in range(NUMBER_OF_DOTS):
	x = random.randint((-SCREEN_WIDTH + 20) + MAXIMUM_BALL_RADIUS, (SCREEN_WIDTH - 20) - MAXIMUM_BALL_RADIUS)
	y = random.randint((-SCREEN_HEIGHT + 20) + MAXIMUM_BALL_RADIUS, (SCREEN_HEIGHT -20)- MAXIMUM_BALL_RADIUS)
	radius = RADIUS_OF_DOTS
	color = (random.random(), random.random(), random.random())
	New_dot = Ball(x,y,0,0,radius,color,"dot")
	DOTS.append(New_dot)




def move_all_balls(sw,sh):
	for i in BALLS:
		i.move(sw,sh)

def collide(ball_a,ball_b):
	if ball_a == ball_b:
		return False
	else:
		ax = ball_a.xcor()
		ay = ball_a.ycor()
		bx = ball_b.xcor()
		by = ball_b.ycor()
		distance = math.sqrt(((ax-bx)**2)+((ay-by)**2))
		if (distance + 10) <= (ball_b.r + ball_a.r):
			return True
		else:
			return False


def dotcollision(ball,dot):
	ax = ball.xcor()
	ay = ball.ycor()
	bx = dot.xcor()
	by = dot.ycor()
	distance = math.sqrt(((ax-bx)**2)+((ay-by)**2))
	if (distance + 10) <= (ball.r + dot.r):
		return True
	else:
		return False

def dotball():
	for ball in BALLS:
		for dot in DOTS:
			if dotcollision(ball,dot):
				ball.r += 1
				ball.shapesize(ball.r/10)
				dot.goto(random.randint(-SCREEN_WIDTH, SCREEN_WIDTH),random.randint(-SCREEN_HEIGHT, SCREEN_HEIGHT))

def myballdot():
	for dot in DOTS:
		if dotcollision(MY_BALL,dot):
			MY_BALL.r += 1
			MY_BALL.shapesize(MY_BALL.r/10)
			dot.goto(random.randint(-SCREEN_WIDTH, SCREEN_WIDTH),random.randint(-SCREEN_HEIGHT, SCREEN_HEIGHT))

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b):
				radius_b1 = ball_a.r
				radius_b2 = ball_b.r
				X_coordinate = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				Y_coordinate = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				X_axis_speed = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				Y_axis_speed = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				Radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				Color = (random.random(), random.random(), random.random())
				if ball_a.r < ball_b.r:
					ball_a.goto(X_coordinate,Y_coordinate)
					ball_a.dx = X_axis_speed
					ball_a.dy = Y_axis_speed
					ball_a.r = Radius
					ball_a.color(Color)
					ball_a.name = Color
					ball_a.shapesize(Radius/10)
					ball_b.r += 4
					ball_a.shapesize(ball_a.r/10)	
				elif ball_b.r < ball_a.r:
					ball_b.x = X_coordinate
					ball_b.y = Y_coordinate
					ball_b.dx = X_axis_speed
					ball_b.dy = Y_axis_speed
					ball_b.r = Radius
					ball_b.color(Color)
					ball_b.name = Color
					ball_b.shapesize(ball_b.r/10)
					ball_a.r += 4
					ball_a.shapesize(ball_a.r/10)
def check_myball_collision():
	for h in BALLS:
		if collide(MY_BALL,h):
			mr = MY_BALL.r
			obr = h.r
			if mr < obr:
				return False
			elif mr > obr:
					h.goto(random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS),random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
					h.dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
					h.dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
					h.r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
					color =((random.random(), random.random(), random.random()))
					h.color(color)
					h.name = color
					MY_BALL.r += 4
					MY_BALL.shapesize(MY_BALL.r/10)
					h.shapesize(h.r / 10)
	return True

def movearound(event):
	X= event.x - SCREEN_WIDTH
	Y= SCREEN_HEIGHT - event.y
	MY_BALL.goto(X,Y)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

def scoreboard():
	score.goto(SCREEN_WIDTH -50 ,pos[1])
	ball1 =[]
	ball2 = BALLS
	for ball3 in ball2:
		score.pencolor("white")
		score.pencolor((ball3.name))
		score.write(str(ball3.r), align = "right", font = ("Arial",20,"normal"))
		score.goto(SCREEN_WIDTH - 50 , score.ycor() - 30)
	score.pencolor((colmb))
	score.write(str(MY_BALL.r), align = "right", font = ("Arial",20,"normal"))



def lost():
	turtle.write("You lost", align = "center", font = ("Arial",30,"normal"))
	while True:
		time.sleep(1)
		break
def won():
	turtle.write("You Won!!", align = "center", font = ("Arial",30,"normal"))
	while True:
		time.sleep(1)
		break

while RUNNING == True:
	move_all_balls(SCREEN_WIDTH,SCREEN_HEIGHT)
	check_all_balls_collision()
	SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
	if check_myball_collision() == False:
		lost()
		break
	elif ((MY_BALL.r >= 150) and (MY_BALL.r > max(BALLS[0].r,BALLS[1].r,BALLS[2].r,BALLS[3].r,BALLS[4].r))):
		won()
		break
	dotball()
	scoreboard()
	myballdot()
	time.sleep(SLEEP)
	turtle.update()
	score.clear()
