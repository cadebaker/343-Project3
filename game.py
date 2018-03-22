from player import *
from neighborhood import * 
from weapon import *
from NPC import *
from observer import *
from home import *

"""******************************************************
*Class that handles an entire game of Zork, utilizing
*several methods and classes
*
*Created by Cade Baker and Megan Thomas, Winter 2018
******************************************************"""
class Game(): 
	
	def __init__(self):
		# variables for a player method, netighborhood method, rows, columns, in the game, and if the player one
		self.player = Player()
		self.neighborhood = Neighborhood()
		self.rows = 0
		self.cols = 0
		self.inGame = 1
		self.wonGame = 0

	#define an introduction method for the user
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
		print(" ")
		print("How large is your neighborhood?")
		
		#ask how many rows and columns the user wants for the neighborhood
		try:
			self.rows = int(input("Number of rows: "))
			self.cols = int(input("Number of columns: "))
		except ValueError:
   			print("Must enter an Integer Value")
   			self.introduction()
			
		#error checking to verify rows and columns are between 1 and 20
		if self.rows < 0 or self.rows > 20 or self.cols < 0 or self.cols > 20:
			print("The number of columns must be more than 0 and less than 20.")
			self.introduction()
		print(" ")
		#create the neighborhood 
		self.neighborhood.createNeighborhood(self.rows,self.cols)

	#define a method to show the possible instructions to the users
	def instructions(self):
		print("The game commands are as follows")
		print("commands : display this commands menu")
		print("location : change your location in the neighborhood")
		print("stats    : shows players statistics")
		print("weapon   : this allows you to your weapon inventory and select the weapon you want to use")
		print("attack   : attack the house we are currently at with your current weapon")
		print("quit     : end game")
		print(" ")

	#define a method for the player to begin his commands
	def promptPlayer(self):
		#ask for user input
		command = input("Enter command: ")

		#handle the command to change location
		if command == "location":
			newRow = 0
			newCol = 0
			#ask user for new location
			newRow = int(input("New Row: "))
			newCol = int(input("New Column: "))

			#check to ensure the row and column exists in the neighborhood
			if newRow >= 0 and newRow < self.rows and newCol >= 0 and newCol < self.cols: 
				#switch location, notify user, and print the neighborhood
				self.player.setLocation(newRow, newCol)

				print("Your new location is: {}".format(self.player.getLocation()))
				print(" ")
				self.neighborhood.printNeighborhood(self.player.getLocation())
			#handle an invalid location
			else:
				print("Not a possible location, please select location again to change")

		#print player stats
		elif command == "stats":
			self.player.printPlayerStats()
			print(" ")

		#handle weapon switching
		elif command == "weapon":
			#show inventory of weapons, uses left, and prompt for weapon switching
			self.player.printInventory()
			print("Your current weapon is : ", self.player.getCurrentWeapon().getWeaponName())
			print("Your uses left: ", self.player.getCurrentWeapon().getUses() )
			option = input("Would you like to change your current weapon? Enter y for yes and n for no: ")
			#switch user weapon if he or she would like
			if option == "y": 
				weaponIndex = int(input("Enter the number of the weapon you would like to use from inventory: "))
				if weaponIndex >= 0 and weaponIndex <= 9:
					self.player.setCurrentWeapon(weaponIndex)
					if self.player.getCurrentWeapon().getUses() <= 0:
						self.player.updateCl()
					print(" ")
					print("Your current weapon is : ", self.player.getCurrentWeapon().getWeaponName())
					print("Your uses left: ", self.player.getCurrentWeapon().getUses() )
				else:
					print("That is not a valid weapon choice. To try again type the weapon command.")
			print(" ")

		#print the instructions for the game
		elif command == "commands":
			self.instructions()
			print(" ")

		#attack the selected house with the current weapon
		elif command == "attack":
			self.fight()
			print(" ")
			self.neighborhood.printNeighborhood(self.player.getLocation())

		#quit the game
		elif command == "quit":
			self.inGame = 0
			self.wonGame = 3

	#define a method for fighting 
	def fight(self):
		#attack current house with current weapon
		currentLocation = self.player.getLocation()
		house = self.neighborhood.getHouse(currentLocation[0], currentLocation[1])
		house.attackHouse(self.player.getCurrentWeapon(), self.player.getAttackValue())
		#add damage to player from the monsters
		damageToPlayer = house.attackPlayer()
		currentHealth = self.player.getHealth() - damageToPlayer

		#update weapon inventory if there are no uses left
		if self.player.getCurrentWeapon().getUses() <= 0:
			self.player.updateCl()
		#update current health if player is alive
		if currentHealth > 0 :
			self.player.setHealth(currentHealth)
		#leave game if player is dead
		else: 
			self.wonGame = 0
			self.inGame = 0
		#leave game if player won
		if self.neighborhood.getTotalNumMonster() == 0:
			self.wonGame = 1
			self.inGame = 0


	#define a method to run the game
	def run(self):
		#show intro, print neighborhood, and print instructions
		self.introduction()
		self.neighborhood.printNeighborhood(self.player.getLocation())
		self.instructions()
		#handle player winning
		if self.neighborhood.getTotalNumMonster() == 0:
			self.wonGame = 1
			self.inGame = 0
		#repeat prompt while user is playing / alive
		while self.inGame == 1:
			self.promptPlayer()
		#handle a win
		if self.wonGame == 1:
			print("Congrats! You defeated all of the monsters")
		#handle a loss
		elif self.wonGame == 0:
			print("You were defeated!")
		#handle a quit
		else:
			print("You quit, Goodbye")
#create a game and run it
g = Game()
g.run()
