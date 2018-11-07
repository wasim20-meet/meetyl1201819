import turtle

#first fun

def right(l):
	if l > 10:
		turtle.forward(l)
		turtle.right(l)
	right(l)
# def back ():


# def left ():
right(200)
turtle.mainloop()