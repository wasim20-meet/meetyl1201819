import turtle
import Tkinter as tk
import tkSimpleDialog as simpledialog
s=turtle.getscreen()
number = 0
turtle.register_shape("wizard.gif")
turtle.bgpic("frame.gif")
WIZARD = turtle.clone()

WIZARD.shape("wizard.gif")

def A():
     global number
     number=1
     return(number)
     print("hi")
def B():
     global number
     number=2
     return(number)
     print("hello")
def C():
     global number
     number=3
     return(number)
     print("hel")
def D():
     global number
     number=4
     return(number)
     print("h")
while True:
     s.onkey(A,"a")
     s.onkey(B,"b")
     s.onkey(C,"c")
     s.onkey(D,"d")
     turtle.listen()

# greeting = simpledialog.askstring("input"," I am the coding wizard!!\nYou think you know computer programming huh?",parent=tk.Tk().withdraw())
# if greeting == "yes":
#      turtle.write("Then lets see what MEET has taught you!!!" , move=False, align="center", font=("Arial", 16 , "bold"))
# turtle.clear()

# if greeting == "no":
#      quit()


class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer







question_prompts= [
"My_list = [prince,[1,2,3],[meet]] is an example of?\n(a)An indxed\n(b)An appended list\n(c)A nested list\n(d)A scliced list",
"Can you find me the word hero from My_Tuple\n('a','z','e','o','y','k','r','j','h','q')","Now find me the word witch but, using negative indexing\nMy_tuple = ('e','t','o','i','h','a','c','l','w')",
"Can you print the words 'Can you beat this game?' using my_function()?",
"Create a large red fire breathing dragon for me named Sadek using inheritance\nUse Animal class for attributes size, color, ability, species and name\nUse description()",
"What will this turtle code print?\nfor i in range(60)\npenup()\ngo to(random.randint(-200, 450),\nrandom.randint(-400, 400))\npendown()\nred = random.randint( 0, 30) / 100\nyellow  = random.randint(50, 100) / 100\nblue = random.randint( 0,  30) / 100\npencolor((red, yellow, blue))\ncircle_size = random.randint(10, 40)\npensize(random.randint(1, 5))\nfor i in range(6):\ncircle(circle_size)\nleft(60)\n(a)Flowers\n(b)Ninja Stars\n(c)Turtles\n(d)Hearts"

]

questions = [
Question(question_prompts[0], "c A nested list"),
Question(question_prompts[1], "print(My_tuple[8]) print(My_tuple[2]) print(My_tuple[6]) print(My_tuple[3])"),
Question(question_prompts[2], "print(My_tuple[-1]) print(My_tuple[-6]) print(My_tuple[-8]) print(My_tuple[-3]) print(My_tuple[-5])"),
Question(question_prompts[3], "def my_function(): print(""Can you beat this game?"") my_function()"),
Question(question_prompts[4], "class Animal(object): def__init__(self,size,color,ability,species,name) self.size = size self.color = color self.ability = ability self.species = species self.name = name def description(self): print (self.size + self.color + self.ability + self.species + ""named"" + self.name) dragon = Animal(""large"", ""red"", ""fire breathing"", ""dragon"", ""Sadek"") dragon.description()"),
Question(question_prompts[5], "a Flowers")]



turtle.mainloop()