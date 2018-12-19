# Name = "Wasim"
# Name100 = Name * 100
# print(Name100)

# number1= 5
# print(number1)
# number2 = 10
# print(number2)

# i2 = 0
# ls1 = [3,6,9]
# i = 0
# while i != 3:
# 	i2 = i2 + ls1[i] 
# 	print(ls1[i])
# 	i = i + 1

# print(i2)

# import turtle
# turtle.begin_fill()
# turtle.goto(0,100)
# turtle.goto(100,100)
# turtle.goto(100,0)
# turtle.goto(0,0)
# turtle.end_fill()
# turtle.mainloop()

# import turtle
# turtle.pencolor("white")
# turtle.penup()
# turtle.goto(-100,50)
# turtle.pendown()
# turtle.begin_fill()
# turtle.circle(75)
# turtle.penup()
# turtle.forward(-25)
# turtle.pendown()
# turtle.circle(100)
# turtle.pencolor("blue")
# turtle.end_fill()
# turtle.mainloop()

import turtle
turtle.speed(100)
list1 = ['blue','black','red','yellow','green']
list2 = [(-110,-25),(135,-25),(375,-25),(15,-100),(250,-100)]
for x in range(len(list1)):
	turtle.pensize(25)
	turtle.penup()
	turtle.goto(list2[x])
	turtle.pendown()
	turtle.color(list1[x])
	turtle.circle(100)
turtle.mainloop()