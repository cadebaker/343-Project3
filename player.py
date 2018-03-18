from observer import *
from random import randint
from weapon import *

class Player(Observable):

	def __init__(self):

		self.health = randint(100,125)
		self.attackValue = randint(10,20)
		self.weapons = [0] * 10 
		self.location = [0,0]

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
		self.currentWeapon = self.weapons[0]
		

	def getHealth(self):
		return self.health

	def setHealth(self, newHealth):
		self.health = newHealth

	def getAttackValue(self):
		return self.attackValue

	def getLocation(self):
		return self.location

	def setLocation(self, newRow, newCol):
		self.location = [newRow, newCol]

	def getInventory(self):
		return weapons

	def getCurrentWeapon(self):
		return currentWeapon

	def setCurrentWeapon(self, index):
		self.currentWeapon = weapons[index]

	def printPlayerStats(self):
		print("Player Stats")
		print("Current Health: %d", self.health)
		print("Current Attack Value: %d", self.attackValue)

	def printInventory(self):

		for index in weapons:
			print("Weapon %d", index)
			print("		  %s : %d uses", weapons[index].getName(), weapons[index].getUses())

	def updateInventory(self):

		for index in weapons:
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



