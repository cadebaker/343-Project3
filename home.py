from observer import *
from random import *
from NPC import *

"""******************************************************
*Class that represents a house
******************************************************"""
class Home(Observer, Observable): 
	
	def __init__(self):
		
		self.numMonsters = randint(0, 10)
		self.monstersInHouse = []
		self.numPeople = 0

		while len(self.monstersInHouse) <= self.numMonsters:

			monsterType = randint(0,4)
			m = Zombie()

			if monsterType == 0:
				m = Zombie()
				self.monstersInHouse.append(m)

			elif monsterType == 1:
				m = Vampire()
				self.monstersInHouse.append(m)

			elif monsterType == 2:
				m = Ghouls() 
				self.monstersInHouse.append(m)

			elif monsterType == 3:
				m = Werewolf()
				self.monstersInHouse.append(m)

			#m.add_observer(self) 
			#print(m.getHealth())


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
	def attackHouse(self, weaponName, attackValue):
		print("number of monsters: {}".format(self.numMonsters))
		
		for monster in range(0, self.numMonsters):
			print("monster {}".format(monster))
			damage = int(self.monstersInHouse[monster].getWeaponDamage(weaponName))
			monsterHealth = self.monstersInHouse[monster].getHealth()
			monsterHealth = monsterHealth - (damage * attackValue)
			print("health before {}".format(self.monstersInHouse[monster].getHealth()))
			print("health after {}".format(monsterHealth))

			if monsterHealth > 0:
				self.monstersInHouse[monster].setHealth(monsterHealth)
			else:
					print("monster killed")
					self.monstersInHouse[monster] = Person()
					self.numMonsters = self.numMonsters - 1
					self.numPeople = self.numPeople + 1


	#method to attack the player 
	def attackPlayer(self):

		damage = 0
		for monster in self.monstersInHouse:
			damage = damage + monster.getAttackStrength()

		return damage
