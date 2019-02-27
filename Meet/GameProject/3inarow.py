from turtle import Turtle 
import math
import turtle
import time
import random
import circle
from circle import Circle
from array import *
turtle.tracer(10,1)
listcol=["sky blue","hot pink","tan","gold"]
turtle.pensize(5)
turtle.penup()
turtle.goto(-500,400)
turtle.pendown()
turtle.speed(0)
#turtle.setup(2000,2000)
times=0
for i in range (4):
	turtle.forward(900)
	turtle.right(90)
for i in range(5):
	turtle.forward(90)
	turtle.right(90)
	turtle.forward(900)
	turtle.left(90)
	turtle.forward(90)
	turtle.left(90)
	turtle.forward(900)
	turtle.right(90)
for i in range(5): # 10 rows
	turtle.right(90)
	turtle.forward(90)
	turtle.right(90)
	turtle.forward(900)
	turtle.left(90)
	turtle.forward(90)
	turtle.left(90)
	turtle.forward(900)
score=0
move_left=25
print("Welcome! You have to get 1,500 points to move left press l to move right press r")
print("Your score is:" + str(score)+ " you have "+str(move_left)+" moves left" )
w, h = 10, 10;
Matrix = [[0 for x in range(w)] for y in range(h)] #making 	2D array 10*10
def make(): #makes the balls
	for row in range(10):
		for col in range(10):
			b1=Circle(row,col)
			b1.speed(0)
			Matrix[row][col]=b1
def middle(i,x):
	ball=Matrix[i][x]
	under_b=Matrix[i-1][x]
	abo_b=Matrix[i+1][x]
	left_b=Matrix[i][x-1]
	right_b=Matrix[i][x+1]
	if ball.color1==under_b.color1==abo_b.color1:
		ball.color1=random.choice(listcol)
		ball.color(ball.color1)
		under_b.color1=random.choice(listcol)
		under_b.color(under_b.color1)
		return(True)
	elif ball.color1==left_b.color1==right_b.color1:
		ball.color1=random.choice(listcol)
		ball.color(ball.color1)
		right_b.color1=random.choice(listcol)
		# right_b.color1=right_b.color
		# right_b.fillcolor(right_b.color)
		right_b.color(right_b.color1)
		return(True)
	return(False)
def up_edge(i,x):#input: row and col in the up/down edge #output:if there are three in a row
	ball=Matrix[i][x]
	left_b=Matrix[i][x-1]
	right_b=Matrix[i][x+1]
	if ball.color1==left_b.color1==right_b.color1:
		ball.color1=random.choice(listcol)
		# ball.color1=ball.color
		# ball.fillcolor(ball.color)
		ball.color(ball.color1)
		right_b.color1=random.choice(listcol)
		# right_b.color1=right_b.color
		# right_b.fillcolor(right_b.color)
		right_b.color(right_b.color1)
		return(True)
	return(False)



def left_edge(i,x):#input: row and col in the left/right edge #output:if there are three in a row
	ball=Matrix[i][x]
	under_b=Matrix[i-1][x]
	abo_b=Matrix[i+1][x]
	if ball.color1==under_b.color1==abo_b.color1:
		ball.color1=random.choice(listcol)
		# ball.color1=ball.color
		# ball.fillcolor(ball.color)
		ball.color(ball.color1)
		under_b.color1=random.choice(listcol)
		# under_b.color1=under_b.color
		# under_b.fillcolor(under_b.color)
		under_b.color(under_b.color1)
		return(True)
	return(False)



def che_3(ball):
	row=ball.row
	col=ball.col
	did_it=False
	if 1<=row and row<=8 and col>=1 and col<=8:#if the ball is in the middle
		 while middle(row,col):
		 	did_it=True
		 	middle(row,col)
	elif (row==9 or row==0) and col>=1 and col<=8: #if the ball is in the upist/downst line
		while up_edge(row,col):
			did_it=True
			up_edge(row,col)
	elif (col==9 or col==0) and row>=1 and row<=8:
		while left_edge(row,col):
			did_it=True
			left_edge(row,col)
	return(did_it)
def clear_bor():
	global times
	is_back=False
	for i in range(10):
		for x in range(10):
			if che_3(Matrix[i][x]):
				is_back=True
				while che_3(Matrix[i][x]):
					che_3(Matrix[i][x])
	if is_back:
		times+=1
		print(times)
		clear_bor()
	else:
		return(is_back)

def movearound(event):
	turtle.penup()
	turtle.hideturtle()
	turtle.goto(event.x-475,405-event.y)
	return(turtle.pos())
def r(): #switch the posion of tlhe bal to the one on it's right
	global score,move_left
	for i in range(10):
		for x in range(10):
			tx=turtle.xcor()
			ty=turtle.ycor()
			mx=Matrix[i][x].xcor()
			my=Matrix[i][x].ycor()
			if abs(tx-mx)<=20 and abs(ty-my)<=20:
				if  i<=8:
					Matrix[i][x].goto(Matrix[i][x].xcor()+90,Matrix[i][x].ycor())  
					Matrix[i+1][x].goto(Matrix[i+1][x].xcor()-90,Matrix[i+1][x].ycor())#switch the place
					tmp = Matrix[i][x]
					Matrix[i][x] = Matrix[i+1][x]#switching the place in the list
					Matrix[i+1][x] = tmp
					t1=times
					clear_bor()
					if t1==times:
						Matrix[i][x].goto(Matrix[i][x].xcor()+90,Matrix[i][x].ycor())  
						Matrix[i+1][x].goto(Matrix[i+1][x].xcor()-90,Matrix[i+1][x].ycor())#switch the place
						tmp = Matrix[i][x]
						Matrix[i][x] = Matrix[i+1][x]#switching the place in the list
						Matrix[i+1][x] = tmp
						move_left-=1
						print("Your score is:" + str(score)+ " you have "+str(move_left)+" moves left")
						clear_bor()
					else:
						move_left-=1
						score+=100
						print("Your score is:" + str(score)+ " you have "+str(move_left)+" moves left")
						
				else:
					move_left-=1
					print("Your score is:" + str(score)+ " you have "+str(move_left)+" moves left")



def l():
	global score,move_left,times#switch the posion of the bal to the one on it's left
	for i in range(10): 
		for x in range(10):
			tx=turtle.xcor()
			ty=turtle.ycor()
			mx=Matrix[i][x].xcor()
			my=Matrix[i][x].ycor()
			if abs(tx-mx)<=20 and abs(ty-my)<=20:
				if  i>=1:
					Matrix[i][x].goto(Matrix[i][x].xcor()-90,Matrix[i][x].ycor())  
					Matrix[i-1][x].goto(Matrix[i-1][x].xcor()+90,Matrix[i][x].ycor())#switch the place
					tmp = Matrix[i][x]
					Matrix[i][x] = Matrix[i-1][x]#switching the place in the list
					Matrix[i-1][x] = tmp
					t1=times
					clear_bor()
					if t1==times:
						Matrix[i][x].goto(Matrix[i][x].xcor()-90,Matrix[i][x].ycor())  
						Matrix[i-1][x].goto(Matrix[i-1][x].xcor()+90,Matrix[i][x].ycor())#switch the place
						tmp = Matrix[i][x]
						Matrix[i][x] = Matrix[i-1][x]#switching the place in the list
						Matrix[i-1][x] = tmp
						move_left-=1
						print("Your score is:" + str(score)+ " you have "+str(move_left)+" moves left" )
					else:
						move_left-=1
						score+=100
						print("Your score is:" + str(score)+ " you have "+str(move_left)+" moves left" )
				else:#happens if i=1
					move_left-=1
					score+=100
					print("Your score is:" + str(score)+ " you have "+str(move_left)+" moves left" )



make()
clear_bor()


while move_left>0:
	turtle.getcanvas().bind("<Motion>", movearound)
	turtle.onkeypress(r,"r")
	turtle.onkeypress(l,"l")
	s= turtle.getscreen()
	turtle.update()
	turtle.listen()
	if score>=1500:
		print("whooooo")

time.sleep(3)
quit()

turtle.mainloop()