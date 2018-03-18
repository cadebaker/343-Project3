from observer import Observer
from player import *

class Neighborhood(Observer):

	def __init__(self):
		self.rows = 0
		self.cols = 0
		self.totalNumMonster = 0

		self.neighborhood = [] 

	def createNeighborhood(self, rows, cols):
		self.rows = rows
		self.cols = cols

		for row in range(0, self.rows):
			self.neighborhood.append([])
			for col in range(0, self.cols):
				self.h = House()
				self.neighborhood[row].append(h)
				self.neighborhood[row][col].add_observer(self)

	def getTotalNumMonster(self):

		return totalNumMonster

	def printNeighborhood(self, location):

		for row in self.neighborhood:
			for col in row: 
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
