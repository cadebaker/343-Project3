from observer import *
from player import *
from home import *

"""******************************************************
*A class that represents the entire neighborhood
******************************************************"""
class Neighborhood(Observer):

	#constructor 
	def __init__(self):
		self.rows = 0
		self.cols = 0
		self.totalNumMonster = 0

		self.neighborhood = [] 

	#creates the neighborhood
	def createNeighborhood(self, rows, cols):
		self.rows = rows
		self.cols = cols

		for row in range(0, self.rows):
			self.neighborhood.append([])
			for col in range(0, self.cols):
				h = Home()
				#h.add_observer(self)
				self.neighborhood[row].append(h)

	#getter for the number of monsters in the neighborhood
	def getTotalNumMonster(self):

		return self.totalNumMonster

	#getter for the number of monsters in the neighborhood
	def getHouse(self, row, col):

		return self.neighborhood[row][col]

	#prints the neighborhood and updates the total number of monsters 
	def printNeighborhood(self, location):
		currentLocation = [0, 0] 

		self.totalNumMonster = 0
		for row in range(0, self.rows):

			for col in range(0, self.cols): 
				currentLocation  = [row, col]
				if col == self.cols-1:
					print(" {}".format(currentLocation))
				else:
					print(" {}".format(currentLocation), end = '' )

			for col in range(0, self.cols):
				if col == self.cols-1:
					print(" _____ ")
				else: 
					print(" _____ ", end = '' )

			for col in range(0, self.cols):
				if col == self.cols-1:
					print("|     |")
				else: 
					print("|     |", end = '' )

			for col in range(0, self.cols): 
				h = self.neighborhood[row][col]
				self.totalNumMonster = self.totalNumMonster + h.getNumMonster()
				if col == self.cols-1:
					if(self.neighborhood[row][col].getNumMonster() != 10):
						print("|  {}  |".format(self.neighborhood[row][col].getNumMonster()))
				
					else:
						print("|  {} |".format(self.neighborhood[row][col].getNumMonster()))
				else:
					if(self.neighborhood[row][col].getNumMonster() != 10):
						print("|  {}  |".format(self.neighborhood[row][col].getNumMonster()), end ='')
				
					else:
						print("|  {} |".format(self.neighborhood[row][col].getNumMonster()), end ='')

			for col in range(0, self.cols): 
				if col == self.cols-1:
					print("|_____|")
				else:
					print("|_____|", end = '' )

			for col in range(0, self.cols): 
				currentLocation  = [row, col]
				if currentLocation == location:
					if col == self.cols-1:
						print("   *   ")
					else:
						print("   *   ", end = '')
				else: 
					if col == self.cols-1:
						print("       ")
					else:
						print("       ", end = '')

			print(" ")
				
