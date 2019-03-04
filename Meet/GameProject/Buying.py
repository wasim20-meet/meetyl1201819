import Tkinter
from Tkinter import Tk
from Tkinter import *
import entity
from entity import *
import Weapons
from Weapons import *
import Armor
from Armor import *
from startButtons import Princess
LevelPrice = 100
def Buy():
	global LevelPrice
	Shop = Tk()

	def WeaponsM():
		Shop.withdraw()
		global WeaponsF
		WeaponsF = Tk()
		WSB = Button(WeaponsF, text = "WoodenSword - 100$", command = WoodenSwordM)
		RGB = Button(WeaponsF, text = "RubberGlove - 200$", command= RubberGloveM)
		ISB = Button(WeaponsF, text = "WoodenSword - 600$", command =IronSwordM)
		WSB.pack()
		RGB.pack()
		ISB.pack()
	def WoodenSwordM():
		WeaponsF.withdraw()
		if Princess.Balance >= 100:
			Princess.EquipWeapon(WoodSword)
			Princess.Balance -= 100
			Princess.attack = Princess.Weapon.damage + (Princess.strength * Princess.level)
	def RubberGloveM():
		WeaponsF.withdraw()
		if Princess.Balance >= 200:
			Princess.EquipWeapon(RubberGlove)
			Princess.Balance -= 200
			Princess.attack = Princess.Weapon.damage + (Princess.strength * Princess.level)
	def IronSwordM():
		WeaponsF.withdraw()
		if Princess.Balance >= 600:
			Princess.EquipWeapon(IronSword)
			Princess.Balance -= 600
			Princess.attack = Princess.Weapon.damage + (Princess.strength * Princess.level)

	def ArmorM():
		Shop.withdraw()
		global ArmorF
		ArmorF = Tk()
		LB = Button(ArmorF, text = "Leather Armor - 200$",command = LeatherM)
		IB = Button(ArmorF, text = "Iron Armor - 400$",command = IronM)
		SB = Button(ArmorF, text = "Steel Armor - 800$",command = SteelM)
		LB.pack()
		IB.pack()
		SB.pack()

	def LeatherM():
		ArmorF.withdraw()
		if Princess.Balance >= 200:
			Princess.EquipArmor(Leather)
			Princess.Balance -= 200
			Princess.defense = Princess.Armor.protection + (Princess.defence * Princess.level)
	def IronM():
		ArmorF.withdraw()
		if Princess.Balance >= 400:
			Princess.EquipArmor(Iron)
			Princess.Balance -= 400
			Princess.defense = Princess.Armor.protection + (Princess.defence * Princess.level)
	def SteelM():
		ArmorF.withdraw()
		if Princess.Balance >= 800:
			Princess.EquipArmor(Steel)
			Princess.Balance -= 800
			Princess.defense = Princess.Armor.protection + (Princess.defence * Princess.level)

	def ManaM():
		Shop.withdraw()
		if Princess.Balance >= 30:
			if Princess.Cmp < Princess.MP:
				Princess.Balance -= 30
				Princess.Cmp = Princess.MP

	def LevelM():
		Shop.withdraw()
		global LevelPrice
		if Princess.Balance >= LevelPrice:
			Princess.Balance -= LevelPrice
			Princess.lvlup()
			LevelPrice += LevelPrice

	WeaponsB = Button(Shop, text = "Weapons", command = WeaponsM)
	ArmorB = Button(Shop, text = "Armor", command = ArmorM)
	ManaB = Button(Shop, text = "ManaRefill - 30$", command = ManaM)
	LevelB = Button(Shop, text = "Level Up - " + str(LevelPrice) + "$", command = LevelM)
	WeaponsB.pack()
	ArmorB.pack()
	ManaB.pack()
	LevelB.pack()

