import turtle
from turtle import *

turtle.tracer(0.0)
class Entity(Turtle):
	def __init__(self,Ctype,HP,Chp,MP,Cmp,defense,strength,effects,Weapon,Armor,Spells,sprite,Inventory,Quests):
		Turtle.__init__(self)
		self.penup()
		self.speed(100)
		self.Ctype = Ctype
		self.HP = HP
		self.Chp = Chp
		self.MP = MP
		self.Cmp = Cmp
		self.Armor = Armor
		self.defense = self.Armor.protection + defense
		self.strength = strength
		self.effects = effects
		self.Weapon = Weapon
		self.attack = self.Weapon.damage + self.strength
		self.shape(sprite)
		self.effects.append(Armor.effect)
		self.effects.append(Weapon.effect)
		self.Inventory = Inventory
		self.Quests = Quests
		self.Spells = Spells
		self.movement = 20

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

		
class Pot(object):
	def __init__ (self, name, Ptype, Quantity, desc):
		self.name = name
		self.Ptype = Ptype
		self.Quantity = Quantity
		self.desc = desc
		self.type = "Potion"

class Effects(object):
	def __init__(self, name, desc):
		self.name = name
		self.desc = desc

