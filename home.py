from observer import *
from random import *

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

	def getNumMonster(self):

		return self.numMonster

	def getMonstersInHouse(self):

		return self.monstersInHouse

	def getNumPeople(self):

		return self.numPeople

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


	def attackPlayer(self):

		damage = 0
		for monster in monstersInHouse:
			damage = damage + monster.getAttackStrength()

