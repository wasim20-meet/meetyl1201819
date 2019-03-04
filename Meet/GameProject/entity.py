import turtle
from turtle import *
turtle.tracer(0.0)

class Entity(Turtle):
	def __init__(self,Ctype,HP,Chp,MP,Cmp,defence,strength,effects,Weapon,Armor,Spells,sprite,Inventory,Quests,Balance,level):
		Turtle.__init__(self)
		self.penup()
		self.speed(100)
		self.level = level
		self.Ctype = Ctype
		self.HP = HP
		self.Chp = Chp
		self.MP = MP
		self.Cmp = Cmp
		self.Armor = Armor
		self.defence = defence
		self.defense = self.Armor.protection + (self.defence * self.level)
		self.strength = strength
		self.effects = effects
		self.Weapon = Weapon
		self.attack = self.Weapon.damage + (self.strength * self.level)
		self.shape(sprite)
		self.effects.append(Armor.effect)
		self.effects.append(Weapon.effect)
		self.Inventory = Inventory
		self.Quests = Quests
		self.Spells = Spells
		self.movement = 20
		self.Balance = Balance

	def lvlup(self):
		self.level += 1
		self.attack = self.Weapon.damage + (self.strength * self.level)
		self.defense = self.Armor.protection + (self.defence * self.level)



	def Attack(self,b):
		if self.attack > b.defense:
			b.Chp -= (self.attack - b.defense)
		else:
			b.Chp -= 1

	def EquipWeapon(self,Weapon):
		self.Weapon = Weapon
		self.effects.append(Weapon.effect)

	def EquipArmor(self,Armor):
		self.Armor =Armor
		self.effects.append(Armor.effect)


class Weapon(object):
	def __init__(self,name,damage,effect):
		self.damage = damage
		self.name = name
		self.effect = effect
		self.type = "Weapon"

class Armor(object):
	def __init__(self,name,protection,effect):
		self.name = name
		self.protection = protection
		self.effect = effect
		self.type = "Armor"

class Effects(object):
	def __init__(self, name, desc):
		self.name = name
		self.desc = desc

