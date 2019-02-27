import turtle
import time
from turtle import *
turtle.bgpic("frame.gif")

wizard = Turtle()
#wizard.hideturtle()
turtle.register_shape("wizard.gif")
wizard.shape("wizard.gif")
wizard.pu()

turtle.hideturtle()
turtle.pu()
turtle.goto(0,-200)
turtle.write("Well done!", align = ("center"), font = ("comic sans MS", 25, "bold"))
	

turtle.mainloop()