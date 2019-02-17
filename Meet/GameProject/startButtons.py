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
import Potion
from Potion import *
global BG



BG = "castleIn.gif"
turtle.penup()
turtle.tracer(0.0)
turtle.bgpic(BG)
turtle.hideturtle()
global Princess
Princess = Entity("Princess",150,150,200,200,20,15,[],Stick,Cape,[],"CharacterRight.gif",[],[])
Princess.effects.append(alive)
Princess.Inventory.append(HealthPotion)

def equipArmor(i):
	Princess.Armor = i
def equipWeapon(i):
	Princess.Weapon = i
def usePot(i):
	pass
def DescM(i):
	DescF = Tk()
	l = Label(DescF,text = i.desc)
def itemM(i):
	itemF = Tk()
	DescB = Button(itemF, text = "Description", command = DescM(i))
	DescB.pack()
	if i.type == "Armor":
		EquipArmorB = Button(itemF, text = "Equip", command = equipArmor(i))
		EquipArmorB.pack()
	elif i.type == "Weapons":
		EquipWeaponB = Button(itemF, text = "Equip", command = equipWeapon(i))
		EquipWeaponB.pack()
	elif i.type == "Potion":
		UsePot = Button(itemF, text = "Use", command = usePot(i))
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

def spellsM():
	spellsF = Tk()
	for i in Princess.Spells:
		l = Label(spellsF, text = i)
		l.pack()

def effectsM():
	effectsF = Tk()
	for i in Princess.effects:
		l = Label(effectsF, text = i.name)
		l.pack()


def InventoryM():
	InventoryF = Tk()
	for i in Princess.Inventory:
		b = Button(InventoryF, text = i.name, command = itemM(i))
		b.pack()

def QuestsM():
	QuestsF = Tk()
	for i in Princess.Quests:
		l = Label(QusetsF, text = i.name)
		l.pack()

def F2():
	global Start
	Start = Tk()
	PrincessB = Button(Start, text = "Princess", command = PrincessM)
	PrincessB.pack()
	InventoryB = Button(Start, text = "Inventory", command =InventoryM )
	InventoryB.pack()
	QuestsB = Button(Start, text = "Quest", command = QuestsM)
	QuestsB.pack()
	effectsB = Button(Start, text = "Effects", command = effectsM)
	effectsB.pack()
	spellsB = Button(Start, text = "Spells", command = spellsM)
	spellsB.pack()
	settingsB = Button(Start, text = "Settings", command = settingsM)
	settingsB.pack()


def PrincessM():
	PrincessF = Tk()
	HPL = Label(PrincessF, text = "HP =" + str(Princess.HP) + "/" + str(Princess.Chp))
	MPL = Label(PrincessF, text = "MP = " + str(Princess.MP) + "/" + str(Princess.Cmp))
	AttackL = Label(PrincessF, text = "Damage =" + str(Princess.attack))
	DefenseL = Label(PrincessF, text = "Defense =" + str(Princess.defense))
	WeaponL = Label(PrincessF, text = "Weapon - " + Princess.Weapon.name)
	ArmorL = Label(PrincessF, text = "Armor - " + Princess.Armor.name)
	MovementL = Label(PrincessF, text = "Movement =" + str(Princess.movement))
	HPL.pack()
	MPL.pack()
	AttackL.pack()
	DefenseL.pack()
	WeaponL.pack()
	ArmorL.pack()
	MovementL.pack()



def save():
	shelfFile = shelve.open('save')
	shelfFile['Screen'] = BG
	shelfFile['PrincessCurrentHP'] = Princess.Chp
	shelfFile['PrincessCurrentMP'] = Princess.Cmp
	shelfFile['Weapon'] = Princess.Weapon
	shelfFile['effects'] = Princess.effects
	shelfFile['Armor'] = Princess.Armor
	shelfFile['Inventory'] = Princess.Inventory
	shelfFile['Quests'] = Princess.Quests
	shelfFile['Position'] = Princess.pos()
	shelfFile['Spells'] = Princess.Spells
	shelfFile['Movement'] = Princess.movement
	shelfFile.close()

def load():
	F2()
	settingsF.withdraw()
	shelfFile = shelve.open('save')
	Princess.effects = shelfFile['effects']
	Princess.Cmp = shelfFile['PrincessCurrentMP']
	Princess.Chp = shelfFile['PrincessCurrentHP']
	Princess.Weapon = shelfFile['Weapon']
	Princess.Armor = shelfFile['Armor']
	Princess.Inventory = shelfFile['Inventory']
	Princess.Quests = shelfFile['Quests']
	Princess.Spells = shelfFile['Spells']
	Princess.movement = shelfFile['Movement']
	turtle.setup(shelfFile['size'][0],shelfFile['size'][1])
	global BG
	BG=shelfFile['Screen']
	turtle.bgpic(BG)
	if BG == "castleIn.gif":
		turtle.setup(740,750)
	if BG == "CastleOut.gif":
		turtle.setup(560,450)
	if BG == "Yard.gif":
		turtle.setup(560,450)
	Princess.goto(shelfFile['Position'][0],shelfFile['Position'][1])
	shelfFile.close()