from observer import Observable
from random import uniform


"""******************************************************
*Class with variables and methods that each weapon will
*use
******************************************************"""
class Weapon(Observable):
	
	#constructor
	def __init__(self):
		super(Weapon, self).__init__()
		self.weaponName = ""
		self.strength = 0
		self.numberOfUses = 0


	#getter for the number of uses 
	def getUses(self):
		if self.numberOfUses <= 0:
			self.update()
			
		return self.numberOfUses

	#getter for the weapon name
	def getWeaponName(self):
		return self.weaponName

	#getter for the weapon strength
	def getStrength(self):
		return self.strength

	#use the weapon 
	def useWeapon(self):
		self.numberOfUses = self.numberOfUses - 1

		if self.numberOfUses <= 0:
			self.update()
	
	def addObs(self, Ob):
		self.add_observer(Ob)


"""******************************************************
*Uses the Weapon class to create a HersheyKiss and store 
*information specifcially for HersheyKisses
******************************************************"""
class HersheyKiss(Weapon):

	def __init__(self):
		Weapon.__init__(self)
		self.weaponName = "HersheyKisses"
		self.strength = 1
		self.numberOfUses = 10000000

"""******************************************************
*Uses the Weapon class to create a SourStraw and store 
*information specifcially for SourStraw
******************************************************"""
class SourStraw(Weapon):

	def __init__(self):
		Weapon.__init__(self)
		self.weaponName = "SourStraws"
		self.strength = uniform(1.0, 1.75)
		self.numberOfUses = 2

"""******************************************************
*Uses the Weapon class to create a ChocolateBar and store 
*information specifcially for ChocolateBar
******************************************************"""
class ChocolateBar(Weapon):

	def __init__(self):
		Weapon.__init__(self)
		self.weaponName = "ChocolateBars"
		self.strength = uniform(2.0, 2.4)
		self.numberOfUses = 4

"""******************************************************
*Uses the Weapon class to create a NerdBomb and store 
*information specifcially for NerdBomb
******************************************************"""
class NerdBomb(Weapon):

	def __init__(self):
		Weapon.__init__(self)
		self.weaponName = "NerdBombs"
		self.strength = uniform(3.5, 5.0)
		self.numberOfUses = 1