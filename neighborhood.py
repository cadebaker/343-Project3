from observer import Observer
from player import *

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
				self.h = House()
				self.neighborhood[row].append(h)
				self.neighborhood[row][col].add_observer(self)

	#getter for the number of monsters in the neighborhood
	def getTotalNumMonster(self):

		return totalNumMonster

	#prints the neighborhood and updates the total number of monsters 
	def printNeighborhood(self, location):

		self.totalNumMonster = 0
		for row in self.neighborhood:
			for col in row: 
				totalNumMonster = totalNumMonster + neighborhood[row][col].getNumMonster()
				print("  %d ", location)
				print("  _____  ")
				print(" |     | ")
				print(" |  %d | ", neighborhood[row][col].getNumMonster())
				print(" |_____| ")


			if player.getLocation() == [row, col]:
				print("    *    ")
			else: 
				print("          ")
				
			print("          ")
