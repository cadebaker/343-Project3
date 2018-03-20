from observer import *
from random import *
from NPC import *

"""******************************************************
*Class that represents a house
******************************************************"""
class Home(Observer, Observable): 
	
	def __init__(self):

		super(Home, self).__init__()
		self.numMonsters = randint(0, 10)
		self.monstersInHouse = []
		self.numPeople = 0

		while len(self.monstersInHouse) < self.numMonsters:

			monsterType = randint(0,4)

			if monsterType == 0:
				m = Zombie()
				m.addOb(self) 
				self.monstersInHouse.append(m)

			elif monsterType == 1:
				m = Vampire()
				m.addOb(self)  
				self.monstersInHouse.append(m)

			elif monsterType == 2:
				m = Ghouls() 
				m.addOb(self) 
				self.monstersInHouse.append(m)

			elif monsterType == 3:
				m = Werewolf()
				m.addOb(self) 
				self.monstersInHouse.append(m)


	#getter for the number of monster 
	def getNumMonster(self):

		return self.numMonsters

	#getter for the list of monsters in the house 
	def getMonstersInHouse(self):

		return self.monstersInHouse

	#getter for the number of people in the house 
	def getNumPeople(self):

		return self.numPeople

	#method to attack all of the monsters inside of the house
	def attackHouse(self, weapon, attackValue):
		
		for monster in range(0, self.numMonsters):
			damage = int(self.monstersInHouse[monster].getWeaponDamage(weapon.getWeaponName()))
			damage = damage * weapon.getStrength()
			mHealth = self.monstersInHouse[monster].getHealth() - (damage * attackValue)
			self.monstersInHouse[monster].setHealth(mHealth)

		weapon.useWeapon()

		

	def updateCl(self):
		for monster in range(0, self.numMonsters):
			if self.monstersInHouse[monster].getHealth() <= 0:
					p = Person()
					self.monstersInHouse[monster] = Person()
					self.numMonsters = self.numMonsters - 1
					self.numPeople = self.numPeople + 1
					p.add_observer(self)
					self.update()



	#method to attack the player 
	def attackPlayer(self):

		damage = 0
		for monster in self.monstersInHouse:
			damage = damage + monster.getAttackStrength()

		return damage