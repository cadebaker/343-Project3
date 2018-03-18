from observer import *
from random import *

"""******************************************************
*Non-player character class. This is used by every type 
*of monster and it is used by people as well.
******************************************************"""
class npc(Observable):

	#constructor
	def __init__(self):
		self.name = ""
		self.health = 0
		self.attackStrength = 0
		self.weaponDamage = {}

	#set the NPC health points
	def setHealth(self, health):
		self.health = health

	#set the NPC attack strength
	def setAttackStrength(self, attackStrength):
		self.attackStrength = attackStrength

	#get the NPC name
	def getName(self):
		return self.name

	#get the health points from the NPC
	def getHealth(self):
		return self.health

	#get the attack strength of the NPC
	def getAttackStrength(self):
		return self.attackStrength

	def getWeaponDamage(self):
		return self.weaponDamage


"""******************************************************
*Uses the Non-player character class to create a Person.
******************************************************"""
class Person(npc):
	def __init__(self):
		super(Person,self).__init__()
		self.name = "Person"
		self.health = 100
		self.attackStrength = -1
		self.weaponDamage = {"HersheyKisses" : 0,
				     "SourStaws": 0,
				     "ChocolateBars" : 0,
				     "NerdBombs" : 0
				    }

"""******************************************************
*Uses the Non-player character class to create a Zombie.
******************************************************"""
class Zombie(npc):
	def __inti__(self):
		super(Zombie,self).__init__()
		self.name = "Zombie"
		self.health = randint(50, 100)
		self.attackStrength = randint(0, 10)
		self.weaponDamage = {"HersheyKisses" : 1,
				     "SourStaws": 2,
				     "ChocolateBars" : 1,
				     "NerdBombs" : 1
				    }
"""******************************************************
*Uses the Non-player character class to create a Vampire.
******************************************************"""
class Vampire(npc):
	def __inti__(self):
		super(Vampire,self).__init__()
		self.name = "Vampire"
		self.health = randint(100, 200)
		self.attackStrength = randint(10, 20)
		self.weaponDamage = {"HersheyKisses" : 1,
				     "SourStaws": 1,
				     "ChocolateBars" : 0,
				     "NerdBombs" : 1
				    }

"""******************************************************
*Uses the Non-player character class to create a Ghoul.
******************************************************"""
class Ghoul(npc):
	def __inti__(self):
		super(Ghoul,self).__init__()
		self.name = "Ghoul"
		self.health = randint(40, 80)
		self.attackStrength = randint(15, 30)
		self.weaponDamage = {"HersheyKisses" : 1,
				     "SourStaws": 1,
				     "ChocolateBars" : 1,
				     "NerdBombs" : 5
				    }

"""******************************************************
*Uses the Non-player character class to create a Werewolf
******************************************************"""
class Werewolf(npc):
	def __inti__(self):
		super(Werewolf,self).__init__()
		self.name = "Werewolf"
		self.health = 200
		self.attackStrength = randint(0, 40)
		self.weaponDamage = {"HersheyKisses" : 1,
				     "SourStaws": 0,
				     "ChocolateBars" : 0,
				     "NerdBombs" : 1
				    }
