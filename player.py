from observer import Observer
from random import randint
from weapon import *

"""******************************************************
*Class that represents the player and all its methods
******************************************************"""
class Player(Observer):

	#constructor 
	def __init__(self):
		Observer().__init__()
		self.health = randint(200,250)
		self.attackValue = randint(10,20)
		self.weapons = [] 
		self.location = [0, 0]
		self.currentWeaponIndex = 0

		#randomly populate the weapons inventory 
		for index in range(0,10):
			weaponType = randint(0, 3)
			if weaponType == 0:
				self.weapons.insert(index, HersheyKiss())
				self.weapons[index].addObs(self)
			elif weaponType == 1:
				self.weapons.insert(index, SourStraw())
				self.weapons[index].addObs(self)
			elif weaponType == 2:
				self.weapons.insert(index, ChocolateBar())
				self.weapons[index].addObs(self)
			elif weaponType == 3:
				self.weapons.insert(index, NerdBomb())
				self.weapons[index].addObs(self)

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
		return self.weapons

	#getter for the current weapon
	def getCurrentWeapon(self):
		return self.currentWeapon

	#setter for the current weapon 
	def setCurrentWeapon(self, index):
		self.currentWeapon = self.weapons[index]
		self.currentWeaponIndex = index

	#use for the current weapon 
	def useCurrentWeapon(self):
		self.currentWeapon.useWeapon()

	#prints the player stats 
	def printPlayerStats(self):
		print("Player Stats")
		print("Current Health: ", self.health)
		print("Current Attack Value: ", self.attackValue)

	#prints the weapon inventory 
	def printInventory(self):
		for index in range(0,len(self.weapons)):
			print("Weapon ", index)
			print("	Name: ", self.weapons[index].getWeaponName())
			print("	Uses Left:", self.weapons[index].getUses())
			print("  ")

	#updates the weapons inventory 
	def updateCl(self):

			#if the weapon uses if 0 we replace it with a random weapon 
				
		weaponType = randint(0, 4)
		if weaponType == 0:
			print(" ")
			print("That was your last {}, your new weapon is HersheyKisses".format(self.weapons[self.currentWeaponIndex].getWeaponName()))
			self.weapons[self.currentWeaponIndex] = HersheyKiss()
		elif weaponType == 1:
			print(" ")
			print("That was your last {}, your new weapon is SourStraws".format(self.weapons[self.currentWeaponIndex].getWeaponName()))
			self.weapons[self.currentWeaponIndex] = SourStraw()
		elif weaponType == 2:
			print(" ")
			print("That was your last {}, your new weapon is ChocolateBars".format(self.weapons[self.currentWeaponIndex].getWeaponName()))
			self.weapons[self.currentWeaponIndex] = ChocolateBar()
		elif weaponType == 3:
			print(" ")
			print("That was your last {}, your new weapon is NerdBomb".format(self.weapons[self.currentWeaponIndex].getWeaponName()))
			self.weapons[self.currentWeaponIndex] = NerdBomb()

		self.setCurrentWeapon(self.currentWeaponIndex)
