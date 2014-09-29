from math import fabs

class Node:
	# Static tile cost as a dictionary
	tileCost = {'w': 100, 'm': 50, 'f': 10, 'g': 5, 'r': 1, '.': 1, 'A': 0, 'B': 0}

	def __init__(self, position, parent=None):
		self.position = position
		self.parent = parent
		self.cost = 0

	# A node is equal to another if they have the same position
	def __eq__(self, other):
		return self.position == other.position

	# Used for debugging
	def __str__(self):
		position = self.position
		return '[' + str(position[0]) + ', ' + str(position[1]) + ']'

	# Manhattan distance is used as the heuristic function
	def heuristic(self, other):
		dx = self.position[0] - other.position[0]
		dy = self.position[1] - other.position[1]

		return fabs(dx) + fabs(dy)

	# Calculate f(score)
	def fScore(self, other):
		return self.cost + self.heuristic(other)

	# Using the tuple of the position as a hash
	def hash(self):
		return (self.position[0], self.position[1])

	# Set total node cost
	def setNodeCost(self, map):
		tileChar = map[self.position[1]][self.position[0]]
		self.cost = self.parent.cost + Node.tileCost[tileChar]