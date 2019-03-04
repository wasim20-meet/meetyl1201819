import Tkinter
from Tkinter import Tk
from Tkinter import *
import entity
from entity import *
import shelve
import Screens
from Screens import *
import turtle
from turtle import *
import Weapons
from Weapons import *
import Armor 
from Armor import *
import Effects
from Effects import *
import random
from intro import wizard
global BG


global Sk
Sk = Entity("Monster",50,50,25,25,3,15,[],Hand,Bone,[],"SkeletonStanding.gif",[],[],random.randint(1,50),random.randint(1,3))

Sk.goto(0,500)

Sk.hideturtle()
BG = "castleIn.gif"
turtle.penup()
turtle.tracer(0.0)
turtle.bgpic(BG)
turtle.hideturtle()
global Princess
Princess = Entity("Princess",150,150,200,200,5,15,[],Stick,Cape,[],"CharacterRight.gif",[],[],1400,1)

def HealSM():
	global HealSF
	HealSF = Tk()
	H10 = Button(HealSF, text = "10", command = Heal10)
	H20 = Button(HealSF, text = "20", command = Heal20)
	H50 = Button(HealSF, text = "50", command = Heal50)
	H100 = Button(HealSF, text = "100", command = Heal100)
	H10.pack()
	H20.pack()
	H50.pack()
	H100.pack()
	Start.withdraw()


def Heal10():
	if Princess.Chp + 10 <= Princess.HP and Princess.Cmp - 5 >= 0:
		Princess.Chp += 10
		Princess.Cmp -= 5	
	elif Princess.Chp + 10 > Princess.HP and Princess.Cmp - 5 >= 0:
		Princess.Chp += Princess.HP - Princess.Chp
		Princess.Cmp -= 5
	HealSF.withdraw()

def Heal20():
	if Princess.Chp + 20 <= Princess.HP and Princess.Cmp - 10 >= 0:
		Princess.Chp += 20
		Princess.Cmp -= 10	
	elif Princess.Chp + 20 > Princess.HP and Princess.Cmp - 10 >= 0:
		Princess.Chp += Princess.HP - Princess.Chp
		Princess.Cmp -= 10
		HealSF.withdraw()

def Heal50():
	if Princess.Chp + 50 <= Princess.HP and Princess.Cmp - 25 >= 0:
		Princess.Chp += 50
		Princess.Cmp -= 25	
	elif Princess.Chp + 50 > Princess.HP and Princess.Cmp - 25 >= 0:
		Princess.Chp += Princess.HP - Princess.Chp
		Princess.Cmp -= 25
		HealSF.withdraw()

def Heal100():
	if Princess.Chp + 100 <= Princess.HP and Princess.Cmp - 50 >= 0:
		Princess.Chp += 100
		Princess.Cmp -= 50
	elif Princess.Chp + 100 > Princess.HP and Princess.Cmp - 50 >= 0:
		Princess.Chp += Princess.HP - Princess.Chp
		Princess.Cmp -= 50
		HealSF.withdraw()


def equipWeapon():
	Princess.Weapon = i #####
def usePot():
	pass
def DescM():
	DescF = Tk()
	l = Label(DescF,text = i.desc) #####
def itemM():
	itemF = Tk()
	DescB = Button(itemF, text = "Description", command = DescM()) #####
	DescB.pack()

	if i.type == "Armor":
		EquipArmorB = Button(itemF, text = "Equip", command = equipArmor()) #####
		EquipArmorB.pack()
	elif i.type == "Weapons":
		EquipWeaponB = Button(itemF, text = "Equip", command = equipWeapon()) #####
		EquipWeaponB.pack()
	elif i.type == "Potion":
		UsePot = Button(itemF, text = "Use", command = usePot()) #####
		UsePot.pack()


def settingsM():
	global settingsF
	settingsF = Tk()
	Start.withdraw()
	quitB = Button(settingsF, text = "quit", command = quit)
	loadB = Button(settingsF, text = "load", command = load)
	saveB = Button(settingsF, text = "save", command = save)
	saveB.pack()
	loadB.pack()


# def spellsM():
	# spellsF = Tk()
	# for i in Princess.Spells:
		# l = Label(spellsF, text = i)
		# l.pack()

# def effectsM():
	# effectsF = Tk()
	# for i in Princess.effects:
		# l = Label(effectsF, text = i.name)
		# l.pack()


# def InventoryM():
	# InventoryF = Tk()
	# for i in Princess.Inventory:
		# b = Button(InventoryF, text = i.name, command = itemM())
		# b.pack()

# def QuestsM():
# 	QuestsF = Tk()
# 	for i in Princess.Quests:
# 		l = Label(QusetsF, text = i.name)
# 		l.pack()

def F2():
	global Start
	global BG
	Start = Tk()
	PrincessB = Button(Start, text = "Princess", command = PrincessM)
	# QuestsB = Button(Start, text = "Quest", command = QuestsM)
	settingsB = Button(Start, text = "Settings", command = settingsM)
	HealBS = Button(Start, text = "Heal", command = HealSM)
	# InventoryB = Button(Start, text = "Inventory", command =InventoryM )
	# effectsB = Button(Start, text = "Effects", command = effectsM)
	# spellsB = Button(Start, text = "Spells", command = spellsM)
	PrincessB.pack()
	# InventoryB.pack()
	# spellsB.pack()
	# effectsB.pack()
	HealBS.pack()
	# QuestsB.pack()
	settingsB.pack()



	
	





def PrincessM():
	PrincessF = Tk()
	LevelL = Label(PrincessF, text = "Level - " + str(Princess.level))
	HPL = Label(PrincessF, text = "HP =" + str(Princess.HP) + "/" + str(Princess.Chp))
	MPL = Label(PrincessF, text = "MP = " + str(Princess.MP) + "/" + str(Princess.Cmp))
	BalanceL = Label(PrincessF, text = "Bal =" + str(Princess.Balance))
	AttackL = Label(PrincessF, text = "Damage =" + str(Princess.attack))
	DefenseL = Label(PrincessF, text = "Defense =" + str(Princess.defense))
	WeaponL = Label(PrincessF, text = "Weapon - " + Princess.Weapon.name)
	ArmorL = Label(PrincessF, text = "Armor - " + Princess.Armor.name)
	MovementL = Label(PrincessF, text = "Movement =" + str(Princess.movement))
	LevelL.pack()
	HPL.pack()
	MPL.pack()
	BalanceL.pack()
	AttackL.pack()
	DefenseL.pack()
	WeaponL.pack()
	ArmorL.pack()
	MovementL.pack()



def save():
	global BG
	shelfFile = shelve.open('save')
	shelfFile['Screen'] = BG
	shelfFile['PrincessCurrentHP'] = Princess.Chp
	shelfFile['PrincessCurrentMP'] = Princess.Cmp
	shelfFile['PrincessTotalHP'] = Princess.HP
	shelfFile['PrincessTotalMP'] = Princess.MP
	shelfFile['Weapon'] = Princess.Weapon
	# shelfFile['effects'] = Princess.effects
	shelfFile['Armor'] = Princess.Armor
	# shelfFile['Inventory'] = Princess.Inventory
	shelfFile['Quests'] = Princess.Quests
	shelfFile['Position'] = Princess.pos()
	# shelfFile['Spells'] = Princess.Spells
	shelfFile['Movement'] = Princess.movement
	shelfFile['Balance'] = Princess.Balance
	shelfFile['Level'] = Princess.level 
	shelfFile['Damage'] = Princess.attack
	shelfFile['Defense'] = Princess.defense
	shelfFile.close()

def load():
	F2()
	settingsF.withdraw()
	shelfFile = shelve.open('save')
	# Princess.effects = shelfFile['effects']
	Princess.HP = shelfFile['PrincessTotalHP']
	Princess.MP = shelfFile['PrincessTotalMP']
	Princess.Cmp = shelfFile['PrincessCurrentMP']
	Princess.Chp = shelfFile['PrincessCurrentHP']
	Princess.Weapon = shelfFile['Weapon']
	Princess.Armor = shelfFile['Armor']
	# Princess.Inventory = shelfFile['Inventory']
	Princess.Quests = shelfFile['Quests']
	# Princess.Spells = shelfFile['Spells']
	Princess.movement = shelfFile['Movement']
	Princess.Balance = shelfFile['Balance']
	Princess.level = shelfFile['Level']
	Princess.attack = shelfFile['Damage']
	Princess.defense = shelfFile['Defense'] 
	turtle.setup(shelfFile['size'][0],shelfFile['size'][1])
	global BG
	BG = shelfFile['Screen']
	turtle.bgpic(BG)
	if BG == "castleIn.gif":
		turtle.setup(740,750)
		wizard.showturtle()
	if BG == "CastleOut.gif":
		turtle.setup(560,450)
		wizard.hideturtle()
	if BG == "Yard1.gif":
		turtle.setup(560,450)
		wizard.hideturtle()
	if BG == "Yard2.gif":
		turtle.setup(560,450)
		wizard.hideturtle()
	if BG == "Yard3.gif":
		turtle.setup(560,450)
		wizard.hideturtle()
	Princess.goto(shelfFile['Position'][0],shelfFile['Position'][1])
	shelfFile.close()