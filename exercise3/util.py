from node import Node
import board

# Check for child nodes in north, east, south and west direction of current node
# Only return nodes that doesn't exist in dictionary and having a legal position
# Return a list of children
def findChildren(map, parent, nodes):
	children = []
	position = parent.position

	north = [position[0], position[1] + 1]
	northNode = Node(north, parent)

	east = [position[0] + 1, position[1]]
	eastNode = Node(east, parent)

	south = [position[0], position[1] - 1]
	southNode = Node(south, parent)

	west = [position[0] - 1, position[1]]
	westNode = Node(west, parent)

	# Append new children
	if board.isLegalPositionOnBoard(map, north) and isNewChild(nodes, northNode):
		children.append(northNode)

	if board.isLegalPositionOnBoard(map, east) and isNewChild(nodes, eastNode):
		children.append(eastNode)

	if board.isLegalPositionOnBoard(map, south) and isNewChild(nodes, southNode):
		children.append(southNode)

	if board.isLegalPositionOnBoard(map, west) and isNewChild(nodes, westNode):
		children.append(westNode)

	return children

# Check that the child doesn't exist already
def isNewChild(nodes, child):
	return not child.hash() in nodes.keys()