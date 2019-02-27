import startButtons
from startButtons import *
import random
import math
global Skeleton
import Screens
from Screens import *
import time
from intro import wizard
healtht = turtle.clone()
ManaPot = turtle.clone()
HealthPot = turtle.clone()
ManaPot.shape("ManaPotion.gif")
HealthPot.shape("HealthPotion.gif")



potposList = []
for i in range(-100,100) :
	if i % 20 == 0 :
		potposList.append(i)


def Potions():
	a = random.randint(0,20)
	if a == 0:
		HealthPot.showturtle()
		HealthPot.goto(random.choice(potposList), random.choice(potposList))
	if a == 20:
		ManaPot.showturtle()
		ManaPot.goto(random.choice(potposList), random.choice(potposList))
def checkPotCol():
	if Princess.pos() == HealthPot.pos():
		Princess.Chp = Princess.HP
		HealthPot.hideturtle()
		HealthPot.goto(1000,0)
	if Princess.pos() == ManaPot.pos():
		Princess.Cmp = Princess.MP
		ManaPot.hideturtle()
		ManaPot.goto(1000,0)
	if ManaPot.pos() == HealthPot.pos():
		HealthPot.goto(HealthPot.pos()[0] + 20, HealthPot.pos()[1])
	if startButtons.BG == "CastleOut.gif":
		if ManaPot.pos()[1] > -20:
			ManaPot.goto(ManaPot.pos()[0], ManaPot.pos()[1] - 100)
		if HealthPot.pos()[1] > -20:
			HealthPot.goto(HealthPot.pos()[0], HealthPot.pos()[1] - 100)

def FightSM():
	global FightingS
	FightingS = Tk()
	HealthL = Label(FightingS, text ="Health = " + str(Princess.Chp) + "/" + str(Princess.HP))
	ManaL = Label(FightingS, text = "Mp = " + str(Princess.Cmp) + "/" + str(Princess.MP))
	AttackB = Button(FightingS, text = "Attack", command = AttackM)
	RunB = Button(FightingS, text = "Run", command = RunM)
	HealB = Button(FightingS, text = "Heal", command = HealM)
	HealthL.pack()
	ManaL.pack()
	AttackB.pack()
	HealB.pack()
	RunB.pack()

def distance(p0, p1):
	return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def Skeleton1():
	Sk.showturtle()
	Sk.shape("SkeletonStanding.gif")


	
def AttackM():
	global BG
	Princess.shape("CharacterAttacking.gif")
	FightingS.withdraw()
	turtle.update()
	time.sleep(1)
	Princess.Attack(Sk)
	Princess.shape("CharacterStandingAttack.gif")
	turtle.update()
	healtht.clear()
	turtle.update()
	healtht.write("Health =" + str(Sk.Chp) + "/" + str(Sk.HP),move = False, align = "center", font = ("Arial",17,"normal"))
	turtle.update()
	if Sk.Chp <= 0:
				BG = oldBG
				startButtons.BG = oldBG
				turtle.bgpic(BG)
				turtle.setup(560,450)
				Princess.shape("CharacterRight.gif")
				Sk.hideturtle()
				Sk.goto(1000,0)
				healtht.clear()
				Princess.Balance += Sk.Balance
				main()
	else:
		WaitM()
		AttackSKM()
	

def WaitM():
	WaitF = Tk()
	WaitL = Label(WaitF, text = "Wait...")
	WaitL.pack()
	turtle.update()
	time.sleep(1)
	WaitF.withdraw()

def AttackSKM():
	global BG
	Sk.shape("SkeletonAttacking.gif")
	turtle.update()
	Sk.Attack(Princess)
	time.sleep(1)
	Sk.shape("SkeletonStandingAttacking.gif")
	turtle.update()
	if Princess.Chp <= 0:
				BG = "castleIn.gif"
				startButtons.BG = "CastleOut.gif"
				turtle.bgpic(BG)
				turtle.setup(560,450)
				Princess.hideturtle()
				Sk.hideturtle()
				healtht.clear()
				turtle.goto(0,0)
				turtle.write("GAME OVER", move = False, align = "center", font = ("Arial",50,"normal"))
	else:
		FightSM()




	


def HealM():
	global HealF
	HealF = Tk()
	H10 = Button(HealF, text = "10", command = Heal10)
	H20 = Button(HealF, text = "20", command = Heal20)
	H50 = Button(HealF, text = "50", command = Heal50)
	H100 = Button(HealF, text = "100", command = Heal100)
	H10.pack()
	H20.pack()
	H50.pack()
	H100.pack()
	FightingS.withdraw()
	

def Heal10():
	if Princess.Chp + 10 <= Princess.HP and Princess.Cmp - 5 >= 0:
		Princess.Chp += 10
		Princess.Cmp -= 5	
	elif Princess.Chp + 10 > Princess.HP and Princess.Cmp - 5 >= 0:
		Princess.Chp += Princess.HP - Princess.Chp
		Princess.Cmp -= 5
	HealF.withdraw()
	WaitM()
	AttackSKM()

def Heal20():
	if Princess.Chp + 20 <= Princess.HP and Princess.Cmp - 10 >= 0:
		Princess.Chp += 20
		Princess.Cmp -= 10	
	elif Princess.Chp + 20 > Princess.HP and Princess.Cmp - 10 >= 0:
		Princess.Chp += Princess.HP - Princess.Chp
		Princess.Cmp -= 10
	HealF.withdraw()
	WaitM()
	AttackSKM()

def Heal50():
	if Princess.Chp + 50 <= Princess.HP and Princess.Cmp - 25 >= 0:
		Princess.Chp += 50
		Princess.Cmp -= 25	
	elif Princess.Chp + 50 > Princess.HP and Princess.Cmp - 25 >= 0:
		Princess.Chp += Princess.HP - Princess.Chp
		Princess.Cmp -= 25
	HealF.withdraw()
	WaitM()
	AttackSKM()

def Heal100():
	if Princess.Chp + 100 <= Princess.HP and Princess.Cmp - 50 >= 0:
		Princess.Chp += 100
		Princess.Cmp -= 50
	elif Princess.Chp + 100 > Princess.HP and Princess.Cmp - 50 >= 0:
		Princess.Chp += Princess.HP - Princess.Chp
		Princess.Cmp -= 50
	HealF.withdraw()
	WaitM()
	AttackSKM()

def RunM():
	global BG
	FightingS.withdraw()
	a = random.randint(0,4)
	if a == 3:
		startButtons.BG = "CastleOut.gif"
		turtle.bgpic(startButtons.BG)
		turtle.setup(560,450)
		Sk.hideturtle()
		Sk.goto(1000,0)
		healtht.clear()
		main()
	else:
		WaitM()
		AttackSKM()

s = turtle.getscreen()
def moveRight():
	Princess.goto(Princess.pos()[0]+Princess.movement,Princess.pos()[1])
	Princess.shape("CharacterRight.gif")
def moveLeft():
	Princess.goto(Princess.pos()[0]-Princess.movement,Princess.pos()[1])
	Princess.shape("CharacterLeft.gif")
def moveUp():
	Princess.goto(Princess.pos()[0],Princess.pos()[1]+Princess.movement)
def moveDown():
	Princess.goto(Princess.pos()[0],Princess.pos()[1]-Princess.movement)
def pos():
	print(Princess.pos())


def movement():
	s.onkey(pos, "p")
	s.onkey(moveLeft, 'a')
	s.onkey(moveRight, 'd')
	s.onkey(moveUp, 'w')
	s.onkey(moveDown, 's')
	if (startButtons.BG == "Fight.gif"):
		s.onkey(FightSM, "f")
	else:
		s.onkey(F2, "f")
	turtle.listen()

def castleIn():
	if startButtons.BG == "castleIn.gif":
		if (Princess.pos()[0] + Princess.movement > 220):
			Princess.goto(Princess.pos()[0]-Princess.movement,Princess.pos()[1])
		if (Princess.pos()[0] - Princess.movement < -220):
			Princess.goto(Princess.pos()[0]+Princess.movement,Princess.pos()[1])
		if (Princess.pos()[1] + Princess.movement > 120):
			Princess.goto(Princess.pos()[0],Princess.pos()[1]-Princess.movement)
		if (Princess.pos()[1] - Princess.movement < -320):
			startButtons.BG = "CastleOut.gif"
			turtle.bgpic(startButtons.BG)
			Princess.goto(0,0)
			turtle.setup(560,450)
			Skeleton1()
			Sk.goto(random.randint(-260,260),-100)
			Potions()
		

def castleOut():
	yListRightCastle = []
	xListDownRightCastle = []
	xListDownLeftCastle = []
	yListLeftCastle = []
	if startButtons.BG == "CastleOut.gif":
		for y in range(0,241):
			for x in range(155,165):
				yListRightCastle.append((x,y))
		for x in range(20,171):
			for y in range(0,10):
				xListDownRightCastle.append((x,y))
		for x in range(-200,20):
			for y in range(0,10):
				xListDownLeftCastle.append((x,y))
		for y in range(0,221):
			for x in range(-200,-190):
				yListLeftCastle.append(((x,y)))
		if Princess.pos() in yListRightCastle:
			Princess.goto(Princess.pos()[0]+Princess.movement,Princess.pos()[1])
		if Princess.pos() in yListLeftCastle:
			Princess.goto(Princess.pos()[0]-Princess.movement,Princess.pos()[1])
		if Princess.pos() in xListDownLeftCastle:
			Princess.goto(Princess.pos()[0],Princess.pos()[1]-Princess.movement)
		if Princess.pos() in xListDownRightCastle:
			Princess.goto(Princess.pos()[0],Princess.pos()[1]-Princess.movement)
		if Princess.pos()[0] + Princess.movement > 280:
			ManaPot.goto(1000,0)
			HealthPot.goto(1000,0)
			Potions()
			startButtons.BG = "Yard1.gif"
			turtle.bgpic(startButtons.BG)
			Princess.goto(-280 + Princess.movement ,Princess.pos()[1])
			Skeleton1()
			Sk.goto(200,0)
			Sk.HP = 100
			Sk.Chp = 100
			Sk.strength = 22
		if Princess.pos()[0] - Princess.movement < -280:
			ManaPot.goto(1000,0)
			HealthPot.goto(1000,0)
			Potions()
			startButtons.BG = "Yard2.gif"
			turtle.bgpic(startButtons.BG)
			Princess.goto(280 - Princess.movement ,Princess.pos()[1])
			Skeleton1()
			Sk.goto(-200,0)
			Sk.HP = 120
			Sk.Chp = 120
			Sk.defence = 12
			Sk.strength = 26
		if Princess.pos()[1] - Princess.movement < -220:
			Sk.hideturtle()
			Sk.goto(1000,0)
			ManaPot.goto(1000,0)
			HealthPot.goto(1000,0)
			Potions()
			Skeleton1()
			Sk.goto(random.randint(-200,200),random.randint(-100,100))
			startButtons.BG = "Yard3.gif"
			turtle.bgpic(startButtons.BG)
			Princess.goto(Princess.pos()[0],220)

	if startButtons.BG == "Yard1.gif":
		if Princess.pos()[0] - Princess.movement < -280:
			Sk.hideturtle()
			Sk.goto(1000,0)
			ManaPot.goto(1000,0)
			HealthPot.goto(1000,0)
			Potions()
			Skeleton1()
			Sk.goto(random.randint(-260,260),-100)
			startButtons.BG = "CastleOut.gif"
			turtle.bgpic(startButtons.BG)
			Princess.goto(280 - Princess.movement ,Princess.pos()[1])
	if startButtons.BG == "Yard2.gif":
		if Princess.pos()[0] + Princess.movement > 280:
			Sk.hideturtle()
			Sk.goto(1000,0)
			ManaPot.goto(1000,0)
			HealthPot.goto(1000,0)
			Skeleton1()
			Sk.goto(random.randint(-260,260),-100)
			Potions()
			startButtons.BG = "CastleOut.gif"
			turtle.bgpic(startButtons.BG)
			Princess.goto(-280 + Princess.movement ,Princess.pos()[1])
	if startButtons.BG == "Yard3.gif":
		if Princess.pos()[1] + Princess.movement > 240:
			Sk.hideturtle()
			Sk.goto(1000,0)
			ManaPot.goto(1000,0)
			HealthPot.goto(1000,0)
			Potions()
			Skeleton1()
			Sk.goto(random.randint(-260,260),-100)
			startButtons.BG = "CastleOut.gif"
			turtle.bgpic(startButtons.BG)
			Princess.goto(Princess.pos()[1],-220 + Princess.movement)

def fightYard():
	if (distance(Princess.pos(),Sk.pos()) < Princess.movement):
		ManaPot.goto(1000,0)
		HealthPot.goto(1000,0)
		global oldBG
		oldBG = startButtons.BG
		Princess.shape("CharacterStandingAttack.gif")
		Sk.shape("SkeletonStandingAttacking.gif")
		turtle.setup(1000,450)
		startButtons.BG = ("Fight.gif")
		turtle.bgpic(startButtons.BG)
		FightSM()
		while True:
			Princess.goto(200,-80)
			Sk.goto(-200,-100)
			turtle.update()
			healtht.goto(-400,-100)
			healtht.pendown()
			healtht.pencolor("Black")
			Sk.penup()


turtle.setup(740,750)
SLEEP = 0.00774

def main():
	while True:
		movement()
		if (distance(Princess.pos(),Sk.pos()) < Princess.movement):
			fightYard()
		castleIn()
		castleOut()
		time.sleep(SLEEP)
		checkPotCol()
		turtle.update()

