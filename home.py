from observer import *
from random import *

"""******************************************************
*Class that represents a house
******************************************************"""
class Home(Observer, Observable): 
	
	def __init__(self):
		
		self.numMonsters = random.randint(0, 10)
		self.monstersInHouse = []
		self.numPeople = 0

		while len(self.monstersInHouse) <= numMonsters:

			monsterType = random.randint(0,5)

			if monsterType == 0:
				m = Zombie()
				self.monstersInHouse.append(m)
				m.add_observer(self) 

			elif monsterType == 2:
				m = Vampire()
				self.monstersInHouse.append(m)
				m.add_observer(self)

			elif monsterType == 3:
				m = Ghoul() 
				self.monstersInHouse.append(m)
				m.add_observer(self) 

			elif monsterType == 4:
				m = Werewolf()
				self.monstersInHouse.append(m)
				m.add_observer(self) 

	#getter for the number of monster 
	def getNumMonster(self):

		return self.numMonster

	#getter for the list of monsters in the house 
	def getMonstersInHouse(self):

		return self.monstersInHouse

	#getter for the number of people in the house 
	def getNumPeople(self):

		return self.numPeople

	#method to attack all of the monsters inside of the house
	def attackHouse(self, weaponName, attackValue):

		for monster in monstersInHouse:
			damages = monster.getWeaponDamage()
			monsterHealth = monster.getHealth()
			monsterHealth = monsterHealth - (damages[weaponName] * attackValue)
			monster.setHealth(monsterHealth)

			if monsterHealth <= 0:
					monster = Person()
					self.numMonster = self.numMonster - 1
					self.numPeople = numPeople + 1

	#method to attack the player 
	def attackPlayer(self):

		damage = 0
		for monster in monstersInHouse:
			damage = damage + monster.getAttackStrength()

