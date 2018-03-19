from player import *
from neighborhood import * 
from weapon import *
from NPC import *
from observer import *
from home import *

class Game(): 
	
	def __init__(self):

		self.rows = 0
		self.cols = 0
		self.inGame = 1
		self.wonGame = 0


	def introduction(self):
		print("Batches of bad candy had transformed your friends and neighbors into all sorts of crazy monsters. ")
		print("Somehow you missed the tainted candy; it is therefore up to you to save your neighborhood and turn everyone back to normal.")
		print("***********ZORK**********")
		print("  [0,0]   [0,1]   [0,2]  ")
		print("  _____   _____   _____  ")
		print(" |     | |     | |     | ")
		print(" |  3  | |  9  | |  0  | ")
		print(" |_____| |_____| |_____| ")
		print("    *                    ")
		print("                         ")
		print("Above is an example of a 1 row 3 column neighborhood.")
		print("Above each house is the address of the house")
		print("The number inside of each house represents the number of monsters inside")
		print("The asterisk infront of the house shows the players current location")
		print("How large is your neighborhood?")
		
		self.rows = int(input("Number of rows: "))
		self.cols = int(input("Number of columns: "))
		if self.rows < 0 or self.rows > 10 or self.cols < 0 or self.cols > 10:
			print("The number of columns must be more than 0 and less than 10.")
			introduction()

		neighborhood.createNeighborhood(self.rows,self.cols)

	def instructions(self):
		print("The game commands are as follows")
		print("commands : display this commands menu")
		print("location : change your location in the neighborhood")
		print("stats    : shows players statistics")
		print("weapon   : this allows you to your weapon inventory and select the weapon you want to use")
		print("attack   : attack the house we are currently at with your current weapon")
		print("quit     : end game")

	def promptPlayer(self):
		command = input("Enter command: ")

		if command == "location":
			newRow = 0
			newCol = 0
			newRow = int(input("New Row: "))
			newCol = int(input("New Column: "))

			if newRow < 0 and newRow >= self.rows and newCol < 0 and newCol >= self.cols: 
				player.setLocation(newRow, newCol)

		elif command == "stats":
			player.printPlayerStats()

		elif command == "weapon":
		
			player.printInventory()
			print("Your current weapon is : ", player.getCurrentWeapon().getWeaponName())
			print("Your uses left: ", player.getCurrentWeapon().getUses() )
			option = input("Would you like to change your current weapon? Enter y for yes and n for no: ")
			if option == "y": 
				weaponIndex = int(input("Enter the number of the weapon you would like to use from inventory: "))
				if weaponIndex > 0 and weaponIndex < 9:
					player.setCurrentWeapon(weaponIndex)
					print("Your current weapon is : ", player.getCurrentWeapon().getWeaponName())
					print("Your uses left: ", player.getCurrentWeapon().getUses() )
				else:
					print("That is not a valid weapon choice. To try again type the weapon command.")

		elif command == "commands":
			self.instructions()

		elif command == "attack":
			self.fight()

		elif command == "quit":
			self.inGame = 0
			self.wonGame = 3


	def fight(self):

		currentLocation = player.getLocation()
		house = neighborhood.getHouse(currentLocation[0], currentLocation[1])
		house.attackHouse(player.getCurrentWeapon().getWeaponName(), player.getAttackValue())
		damageToPlayer = house.attackPlayer()
		currentHealth = player.getHealth() - damageToPlayer

		if currentHealth > 0 :
			player.setHealth(currentHealth)

		else: 
			self.wonGame = 0
			self.inGame = 0

		if neighborhood.getTotalNumMonster() == 0:
			self.wonGame = 1
			self.inGame = 0



	def run(self):

		self.introduction()
		neighborhood.printNeighborhood(player.getLocation())
		self.instructions()

		while self.inGame == 1:
			neighborhood.printNeighborhood(player.getLocation())
			self.promptPlayer()

		if self.wonGame == 1:
			print("Congrats! You defeated all of the monsters")

		elif self.wonGame == 0:
			print("You were defeated!")

		else:
			print("You quit")

player = Player()
neighborhood = Neighborhood()
g = Game()
g.run()
