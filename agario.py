import turtle 
import ball
import random
from ball import Ball
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

# MY_BALL = Ball()

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5 
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = []

for n in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	new_ball = Ball(x,y,dx,dy,radius,color)
	BALLS.append(new_ball)

def move_all_balls(sw,sh):
	for i in BALLS:
		i.move(sh,sw)

def collide(ball_a,ball_b):
	if ball_a == ball_b:
		return False
	else:
		ax = ball_a.xcor()
		ay = ball_a.ycor()
		bx = ball_b.xcor()
		by = ball_b.ycor()
		distance = math.sqrt((ax-bx**2)+((ay-by)**2))
		if (distance + 10) <= (ball_b.r + ball_a.r):
			return True
		else:
			return False

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
					ball_a.x = X_coordinate
					ball_a.y = Y_coordinate
					ball_a.dx = X_axis_speed
					ball_a.dy = Y_axis_speed
					ball_a.r = Radius
					ball_a.color(Color)
					ball_a.shapesize(Radius/10)
					ball_b.r =+ 1
					ball_b.shapesize(ball_b.r / 10)
				else if ball_b.r < ball_a.r:
					ball_b.x = X_coordinate
					ball_b.y = Y_coordinate
					ball_b.dx = X_axis_speed
					ball_b.dy = Y_axis_speed
					ball_b.r = Radius
					ball_b.color(Color)
					ball_b.shapesize(Radius/10)
					ball_a.r =+ 1
					ball_a.shapesize(ball_a.r / 10)

turtle.mainloop()
