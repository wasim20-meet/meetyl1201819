import turtle
import Tkinter as tk
import tkSimpleDialog as simpledialog
import time
import Screens
from moveFunctions import wizard
from startButtons import winning

TIME=2
turtle1 = turtle.clone()
score = 0
is_did=False
turtle.register_shape("wizard.gif")
wizard.shape("wizard.gif")
turtle.bgpic("frame.gif")
s = turtle.getscreen()
import string
import Tkinter as tk
import tkSimpleDialog as simpledialog

greeting = simpledialog.askstring("input"," I am the coding wizard!!\nYou think you know computer programming huh?",parent=tk.Tk().withdraw())
if greeting == "yes":
     turtle.write("Then lets see what MEET has taught you!!!" , move=False, align="center", font=("Arial", 16 , "bold"))
turtle.clear()

if greeting == "no":
     quit()


class Question:
     def __init__(self, prompt,a,b,c,d,anind):
          self.prompt = prompt
          self.a = a
          self.b=b
          self.c=c
          self.d=d
          self.anind=anind
pro = ["My_list = [prince,[1,2,3],[meet]] is an example of?","Can you print me the word hero from My_Tuple ('e','h','o','r')","Now find me the letter I using negative indexing? list_letters=[w,i,t,c,h]","what the differnce between tupels and lists?","How do you begin a function?","What will this turtle code print?\nfor i in range(60)\npenup()\ngo to(random.randint(-200, 450),\nrandom.randint(-400, 400))\npendown()\nred = random.randint( 0, 30) / 100\nyellow  = random.randint(50, 100) / 100\nblue = random.randint( 0,  30) / 100\npencolor((red, yellow, blue))\ncircle_size = random.randint(10, 40)\npensize(random.randint(1, 5))\nfor i in range(6):\ncircle(circle_size)\nleft(60)"]
a_ans=["An indexed","My_Tuple[0]My_Tuple[2]My_Tuple[3]My_Tuple[0]","list_letters[-4]","list are numbers and tupels are letters","By writing: function","Flowers"]
b_ans=["An appended list","My_Tuple[1]My_Tuple[0]My_Tuple[3]My_Tuple[2]","list_letters[-1]","list are not able to change and tupels are","By writing: def","Ninja Stars"]
c_ans=["A nested list","My_Tuple[1]My_Tuple[2]My_Tuple[3]My_Tuple[4]","list_letters[0]","list has an index and tupels does not","By writing the description of it","Turtles"]
d_ans=["A sliced list","My_Tuple[-2]My_Tuple[0]My_Tuple[2]My_Tuple[3]","list_letters[-3]","tupels are not able to change and list are","By writing: y1 is the best!","Sadeq"]
ans=["c","b","a","d","b","a"]
list_q=[]
for i in range(6):
     q1= Question(pro[i],a_ans[i],b_ans[i],c_ans[i],d_ans[i],ans[i])
     list_q.append(q1)
for i in range(6):
     global score
     is_did=False
     print(list_q[i].prompt)
     print(list_q[i].a)
     print(list_q[i].b)
     print(list_q[i].c)
     print(list_q[i].d)
     answer =simpledialog.askstring("Input", "Enter the letter of the right answer", parent=tk.Tk().withdraw())
     if answer==list_q[i].anind:
          print("wow!")
          score+=1
          print(score)
          time.sleep(TIME)
if score >= 5:
     turtle.bgpic("castleIn.gif")
     from startButtons import Princess
     Princess.showturtle()
     from moveFunctions import main
     from startButtons import winning
     winning += 1
     import end_story
