# Read the board from file and return it as a two dimensional list
def readBoardFromFile(fileName):
	file = open(fileName)
	board = []
	for line in file:
		appendLine = []
		for char in line.strip():
			appendLine.append(char)
		board.append(appendLine)
	file.close()

	return board

# Find the position of the start character
def findStart(board):
	startChar = 'A'
	return findCharInBoard(board, startChar)

# Find the position of the goal character
def findGoal(board):
	goalChar = 'B'
	return findCharInBoard(board, goalChar)

# Find position of a character and return the positon as
# list [x, y]
def findCharInBoard(board, char):
	# Check every character for a match against the char parameter
	for line in xrange(len(board)):
		for i in xrange(len(board[line])):
			if board[line][i] == char:
				return[i, line]

# Check if a given coordinate exists on the map
def isLegalPositionOnBoard(map, position):
	# Only positions inside the map boundaries is legal
	if position[0] < 0:
		return False
	elif position[0] >= len(map[0]):
		return False
	elif position[1] < 0:
		return False
	elif position[1] >= len(map):
		return False

	# Only legal if character == '.'
	char = map[position[1]][position[0]]
	return char != '#'

# Using linked list to generate the path. The shortest path is drawn with '+'
def createShortestPath(map, node):
	# Calculate total cost
	totalPathCost = node.cost
	print('Total cost of the path: ' + str(totalPathCost))

	node = node.parent
	while node.parent:
		map[node.position[1]][node.position[0]] = '+'
		node = node.parent	

def setClosedNode(map, node):
	char = 'x'
	setCharOnBoard(map, node, char)

def setOpenNode(map, node):
	char = '*'
	setCharOnBoard(map, node, char)

# Change the char value on the map given by the nodes position
def setCharOnBoard(map, node, char):
	x = node.position[0]
	y = node.position[1]
	if map[y][x] != 'A' and map[y][x] != 'B':
		map[y][x] = char


def printBoard(board):
	for line in board:
		print(''.join(line)) 
