import turtle
import time
import random
from turtle import *

turtle.bgpic("frame.gif")

prince = Turtle()
prince.hideturtle()
turtle.register_shape("prince.gif")
prince.shape("prince.gif")
prince.pu()
prince.goto(150, -200)
prince.showturtle()


turtle.hideturtle()
turtle.write("YOU WON!!!", align = ("center"), font = ("comic sans MS", 25, "bold"))

for i in range(15):
	time.sleep(0.1)
	turtle.bgcolor(random.random(),random.random(),random.random())
turtle.mainloop()