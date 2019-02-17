import startButtons
from startButtons import *
import turtle
from turtle import *
import time
import moveFunctions
from moveFunctions import *
turtle.setup(740,750)
SLEEP = 0.00774

while True:
	movement()
	castleIn()
	castleOut()
	time.sleep(SLEEP)
	turtle.update()
turtle.mainloop()