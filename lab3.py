import turtle
# turtle.register_shape("square.gif")
# turtle.shape("square.gif")
turtle.speed(0)
turtle.tracer(100)
while True:
	turtle.left(0.1)
	turtle.pendown()
	turtle.forward(200)
	turtle.right(45)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(50)
	turtle.penup()
	turtle.goto(0,0)

turtle.mainloop()
