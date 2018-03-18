from observer import *
from random import randint
from weapon import *

"""******************************************************
*Class that represents the player and all its methods
******************************************************"""
class Player(Observable):

	#constructor 
	def __init__(self):

		self.health = randint(100,125)
		self.attackValue = randint(10,20)
		self.weapons = [0] * 10 
		self.location = [0,0]

		#randomly populate the weapons inventory 
		for index in range(0,11):
			self.weaponType = randint(0, 5)
			if self.weaponType == 1:
				self.weapons.insert(index, HersheyKiss())
			elif self.weaponType == 2:
				self.weapons.insert(index, SourStraw())
			elif self.weaponType == 3:
				self.weapons.insert(index, ChocolateBar())
			elif self.weaponType == 4:
				self.weapons.insert(index, NerdBomb())

		#set the current weapon to be the first weapon in the inventory 		
		self.currentWeapon = self.weapons[0]
		

	#getter for the players health 
	def getHealth(self):
		return self.health

	#setter for the players health 
	def setHealth(self, newHealth):
		self.health = newHealth

	#getter for the attack value
	def getAttackValue(self):
		return self.attackValue

	#getter for the player location 
	def getLocation(self):
		return self.location

	#set the players new location 
	def setLocation(self, newRow, newCol):
		self.location = [newRow, newCol]

	#getter for the weapons inventory
	def getInventory(self):
		return weapons

	#getter for the current weapon
	def getCurrentWeapon(self):
		return currentWeapon

	#setter for the current weapon 
	def setCurrentWeapon(self, index):
		self.currentWeapon = weapons[index]

	#prints the player stats 
	def printPlayerStats(self):
		print("Player Stats")
		print("Current Health: %d", self.health)
		print("Current Attack Value: %d", self.attackValue)

	#prints the weapon inventory 
	def printInventory(self):

		for index in weapons:
			print("Weapon %d", index)
			print("		  %s : %d uses", weapons[index].getName(), weapons[index].getUses())

	#updates the weapons inventory 
	def updateInventory(self):

		for index in weapons:

			#if the weapon uses if 0 we replace it with a random weapon 
			if weapons[index].getUses() == 0: 
		
				self.weaponType = randInt(0, 5)
				if weaponType == 1:
		 			weapons[index] = HersheyKiss()
				elif weaponType == 2:
					weapons[index] = SourStraws()
				elif weaponType == 3:
					weaponType[index] = ChocolateBar()
				else:
					weaponType[index] = NerdBomb()



