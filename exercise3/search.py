from heapq import heappush, heappop, heapify
from aStar import aStar
from dijkstra import dijkstra
from bfs import bfs
import board
from node import Node

# Run BFS
def doBfs(map, startNode, goalNode):	
	print('BFS algorithm')

	# Start the search
	map, numberOfOpenNodes, numberOfClosedNodes = bfs(map, startNode, goalNode)
	printMap(map, numberOfOpenNodes, numberOfClosedNodes)

# Run Dijkstra
def doDijkstra(map, startNode, goalNode):	
	print('Dijkstra algorithm')
	
	# Start the search
	map, numberOfOpenNodes, numberOfClosedNodes = dijkstra(map, startNode, goalNode)
	printMap(map, numberOfOpenNodes, numberOfClosedNodes)

# Run A*
def doAStar(map, startNode, goalNode):	
	print('A* algorithm')
	
	# Start the search
	map, numberOfOpenNodes, numberOfClosedNodes = aStar(map, startNode, goalNode)
	printMap(map, numberOfOpenNodes, numberOfClosedNodes)

# All the search algoritms returns the edited map and total number of
# opened and closed nodes.
def printMap(map, numberOfOpenNodes, numberOfClosedNodes):
	print('Number of closed nodes: ' + str(numberOfClosedNodes))
	print('Number of opened nodes: ' + str(numberOfOpenNodes))
	board.printBoard(map)	
	print('__________________________________________')
	print('')

def main():
	# Find shortest path on all the boards
	boards = ['boards/board-1-1.txt', 'boards/board-1-2.txt', 'boards/board-1-3.txt', 'boards/board-1-4.txt', 'boards/board-2-1.txt', 'boards/board-2-2.txt', 'boards/board-2-3.txt', 'boards/board-2-4.txt']
	for i in xrange(len(boards)):
		print(str(i) + ': ' + boards[i])
		
	boardNumber = int(raw_input('Enter board number: '))
	print('')
	
	# Read the board from file
	dijkstraMap = board.readBoardFromFile(boards[boardNumber])
	bfsMap = board.readBoardFromFile(boards[boardNumber])
	astarMap = board.readBoardFromFile(boards[boardNumber])

	# Get start and goal node
	startNode = Node(board.findStart(bfsMap))
	goalNode = Node(board.findGoal(bfsMap))

	# Do all the search algoritms
	doBfs(bfsMap, startNode, goalNode)
	doDijkstra(dijkstraMap, startNode, goalNode)
	doAStar(astarMap, startNode, goalNode)

main()