import turtle
from turtle import Turtle
import random 
import math
import time

turtle.tracer(0)
#turtle.speed(1000)
turtle.bgpic("forest.gif")
turtle.hideturtle()
#turtle.tracer(3,500)
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/4
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

OBSTICLES_LIST = []
COINS_LIST = []
SPIKES_LIST = []

OBSTICLES_MAX_NUMBER = 3
#MAX_COINS_NUMBER: 3
MAX_SPIKES_NUMBER = 10
direction = 0
player_lost = False
f_2 = True
flag_1 = False
flag_2 = False
flag_3 = False
flag_4 = False

count = 0
SCORE = 0
class Player(Turtle):
	def __init__(self):
		Turtle.__init__(self)
		self.pu()
		# Graphical parameters
		self.direction = 0
		# Image sizes
		self.Px = 60
		self.Py = 77
		# Player movement
		self.Pdx = 10
		self.Pdy = 0.5
		self.Pminx = -450
		self.Pmaxx =  450
		self.Pminy = -200
		self.Pmaxy =  200

player = Player()
player.hideturtle()
turtle.register_shape("CharacterLeft.gif")
player.shape("CharacterLeft.gif")
player.pensize(100)
player.pu()
player.goto(player.Pminx, player.Pminy)
player.showturtle()


def move_Right():
	global direction, player, flag_3
	if player.xcor() + 30 > (2 * SCREEN_WIDTH):
		flag_3 = True
		if flag_3:
			return
	else:
		direction = 1
		x=player.pos()[0]
		y=player.pos()[1]
		player.goto(x+player.Pdx,y)
		return direction
def move_Left():
	global direction, player, flag_4, SCREEN_WIDTH
	if player.xcor() - 30 < -(2 * SCREEN_WIDTH):
		flag_4 = True
		if flag_4:
			return
	else:
		direction = 2
		x=player.pos()[0]
		y=player.pos()[1]
		player.goto(x-player.Pdx,y)
		return direction
def move_Up():
	global direction, player, flag_1 
	if player.ycor() + 38.5 > SCREEN_HEIGHT:
		flag_1 = True
		if flag_1:
			return
	else:
		direction = 3
		x=player.pos()[0]
		y=player.pos()[1]
		player.goto(x,y+player.Pdy*10)
		return direction

def move_Down():
	global direction, player, flag_2, f_2
	f_2 = False
	check_obsticle_col(OBSTICLES_LIST)
	if f_2:
		return
	if player.ycor() - 38.5 < player.Pminy:
		flag_2 = True
		if flag_2:
			return
	else: 
		direction = 4
		x=player.pos()[0]
		y=player.pos()[1]
		player.goto(x,y-player.Pdy/5)
		return direction

class obsitcles(Turtle):
	def __init__(self,x,dx):
		Turtle.__init__(self)
		self.hideturtle()
		self.pu()
		self.width = 100
		self.height = 20
		self.x = x
		self.y = random.randint((-200 + 70),(SCREEN_HEIGHT - 150))
		self.dx = random.randint(1,2)/10
		self.shape("square")
		self.resizemode("user")
		self.shapesize(1, 4)
		self.goto(self.x,self.y)
		self.showturtle()

	def move(self):
		global OBSTICLES_LIST
		x = self.pos()[0]
		y = self.pos()[1]
		self.goto(x - self.dx, y)
		for obsticle in (OBSTICLES_LIST):
			if obsticle.xcor() < -(2 * SCREEN_WIDTH):
				OBSTICLES_LIST.remove(obsticle)
				obsticle.hideturtle()
				turtle.update()

class coins(Turtle):
	def __init__(self, x, y, dx):
		Turtle.__init__(self)
		self.hideturtle()
		self.pu()
		self.x = x
		self.y = y
		self.dx = dx
		self.goto(self.x,self.y)
		self.showturtle()

	def move_coins(self, COINS_LIST):
		global OBSTICLES_LIST
		x = self.pos()[0]
		y = self.pos()[1]
		self.goto(x - self.dx, y)
		for coin in (COINS_LIST):
			if coin.xcor() < -(2 * SCREEN_WIDTH):
				COINS_LIST.remove(coin)
				coin.hideturtle()
				turtle.update()

class spikes(Turtle):
	def __init__(self):
		Turtle.__init__(self)
		self.hideturtle()
		self.pu()
		self.x = random.randint(-SCREEN_HEIGHT, SCREEN_HEIGHT)
		self.y = -SCREEN_HEIGHT + 210
		self.dx  = random.randint(1,20)
		self.goto(self.x,self.y)
		self.showturtle()


def make_spikes(SPIKES_LIST):
	new_spike = spikes()
	for spike in (SPIKES_LIST):
		if spike.pos() in player.pos():
			SPIKES_LIST.remove(new_spike)

	turtle.register_shape("spike.gif")
	new_spike.shape("spike.gif")
	SPIKES_LIST.append(new_spike)
	turtle.update()


def make_objects(OBSTICLES_LIST):
	global OBSTICLES_MAX_NUMBER
	new_obsticle = obsitcles(500,1)
	OBSTICLES_LIST.append(new_obsticle)

	x_coin = random.randint(-4,4)
	new_coin = coins(new_obsticle.xcor() + x_coin, new_obsticle.ycor()+20, new_obsticle.dx)
	turtle.register_shape("coin.gif")
	new_coin.shape("coin.gif")
	COINS_LIST.append(new_coin)
	turtle.update()

def check_obsticle_col(OBSTICLES_LIST):
	global f_2
	for obsticle in (OBSTICLES_LIST):
		if collide(player, obsticle):
			if player.ycor() > obsticle.ycor():
				f_2 = True
				return f_2
			if player.ycor() < obsticle.ycor():
				player.goto(player.xcor(), player.ycor() - 5)
				return True
			return False
def check_coin_col(COINS_LIST):
	for coin in (COINS_LIST):
		if collide(player, coin):
			coin.hideturtle()
			COINS_LIST.remove(coin)
			turtle.clear()
			score_update()
def collide(block_a, block_b):
	block_a_top = block_a.ycor() + 38.5
	block_a_bottom = block_a.ycor() - 38.5
	block_a_right = block_a.xcor() + 30
	block_a_left = block_a.xcor() - 30

	block_b_top = block_b.ycor() + 0.5
	block_b_bottom = block_b.ycor() - 0.5
	block_b_right = block_b.xcor() + 2
	block_b_left = block_b.xcor() - 2
	
	if block_a_top >= block_b_bottom and block_a_bottom <= block_b_top and block_a_right >= block_b_left and block_a_left <= block_b_right:
		return True
	return False
def score_update():
	global SCORE
	turtle.hideturtle()
	turtle.penup()
	SCORE += 10
	turtle.clear()
	turtle.goto(-400,300)
	turtle.color("white")
	turtle.write("Score: " + str(SCORE), font = ("Arial", 30, "bold"))
	if SCORE == 100:
		winning_banner()
def winning_banner():
	turtle.clear()
	turtle.goto(0,0)
	turtle.write("YOU WON!", align = ("center"), font = ("Arial", 50, "bold"))
	print("You won! Well done!!!")
	time.sleep(3) 
	turtle.clear()
	quit()#=============================================================> first quit!

def check_player_lost():
	global player_lost
	for spike in (SPIKES_LIST):
		if collide(player, spike):
			player_lost = True
			turtle.clear()
			turtle.goto(0,0)
			turtle.color("red")
			turtle.write("You lost", align = ("center"), font = ("Arial", 50, "bold"))
			time.sleep(3)
			print("YOU LOST")
			quit()#======================================================>second one!

s = turtle.getscreen()

s.onkeypress(move_Right,'Right')
s.onkeypress(move_Left,'Left')
s.onkeypress(move_Up, 'Up')
s.onkeypress(move_Down, 'Down')
turtle.update()

Pfall = 100
s.listen()

def mario_main()
	while True:
		turtle.update() 
		check_player_lost()
		if direction == 3:
			Pfall = 100
		else:
			Pfall = max(Pfall - 1, 0)
		if Pfall == 0:
			move_Down()

		direction = 0	
		for obsticle in (OBSTICLES_LIST):
			obsticle.move()
			check_obsticle_col(OBSTICLES_LIST)

		for coin in (COINS_LIST):
			coin.move_coins(COINS_LIST)
			check_coin_col(COINS_LIST)

		while len(SPIKES_LIST) < MAX_SPIKES_NUMBER:
			make_spikes(SPIKES_LIST)

		while len(OBSTICLES_LIST) < OBSTICLES_MAX_NUMBER:
			make_objects(OBSTICLES_LIST)
	
	



turtle.mainloop()