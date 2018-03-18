from player import *
from neighborhood import * 
from weapon import *
from NPC import *
from observer import *
from home import *


"""******************************************************
*Runs the entire game function 
******************************************************"""
class Game(): 
	
	#constructor
	def __init__(self):

		self.player = Player()
		self.neighborhood = Neighborhood()
		self.rows = 0
		self.cols = 0
		self.inGame = 1
		self.wonGame = 0

	#prints the introduction to the game and sets the neighborhood size 
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
		
		self.rows = input("Number of rows: ")
		self.cols = input("Number of columns: ")
		if self.rows < 0 or self.rows > 10 or self.cols < 0 or self.cols > 10:
			print("The number of columns must be more than 0 and less than 10.")
			introduction()

		self.neighborhood.createNeighborhood(rows,cols)

	#prints the commands menu 
	def instructions(self):
		print("The game commands are as follows")
		print("commands : display this commands menu")
		print("location : change your location in the neighborhood")
		print("stats    : shows players statistics")
		print("weapon   : this allows you to your weapon inventory and select the weapon you want to use")
		print("attack   : attack the house we are currently at with your current weapon")
		print("quit     : end game")

	#prompts the player for next move
	def promptPlayer(self):
		self.command = raw_input("Enter command: ")

		if command == "location":
			newRow = input("New Row: ")
			newCol = input("New Column: ")

			if newRow > 0 and newRow <= rows and newCol > 0 and newCol <= cols: 
				player.setLocation(newRow, newCol)
				self.neighborhood.printNeighborhood(player.getLocation())

		elif command == "stats":
			player.printPlayerStats()

		elif command == "weapon":
			currentWeapon =  player.getCurrentWeapon()
			player.getInventory()
			print("Your current weapon is : %s", currentWeapon.getWeaponName())
			print("You currently have %d uses left", player.getCurrentWeapon().getUses() )
			option = raw_input("Would you like to change your current weapon? Enter y for yes and n for no ")
			if option == "y": 
				weaponIndex = input("Enter the number of the weapon you would like to use from inventory: ")
				if weaponIndex > 0 and weaponIndex < 10:
					player.setCurrentWeapon(weaponIndex)
				else:
					print("That is not a valid weapon choice. To try again type the weapon command.")

		elif command == "commands":
			self.instructions()

		elif command == "attack":
			self.fight()

		elif command == "quit":
			self.inGame = 0


	#handles the fights when the player attacks 
	def fight(self):

		currentLocation = self.player.getLocation()
		house = self.neighborhood[currentLocation[0]][currentLocation[1]]
		house.attackHouse(player.getCurrentWeapon().getWeaponName(), player.getAttackValue())
		house.attackPlayer()
		
		if currentHealth > 0 :
			player.setHealth(currentHealth)

		else: 
			self.wonGame = 0
			self.inGame = 0

		if self.neighborhood.getTotalNumMonster() == 0:
			self.wonGame = 1
			self.inGame = 0


	#runs the entire game 
	def run(self):

		self.introduction()
		self.instructions()

		while self.inGame == 1:
			self.neighborhood.printNeighborhood(player.getLocation())
			promptPlayer()

		if self.wonGame == 1:
			print("Congrats! You defeated all of the monsters")

		else:
			print("You were defeated!")

g = Game()
g.run()



