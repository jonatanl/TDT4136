from heapq import heappush, heappop, heapify
import board
from node import Node
from util import *

def dijkstra(map, startNode, goalNode):
	# Generate value to hash
	hash = startNode.hash()
	# Min heap with fScore as the value. heap only contains open nodes
	heap = [(startNode.fScore(goalNode), hash)]

	# All open and closed nodes is in the dictionary
	nodes = {startNode.hash(): startNode}

	# Count the total number of closed nodes
	numberOfClosedNodes = 0

	# Run while there still exist opened nodes	
	while len(heap) > 0:
		numberOfClosedNodes += 1

		# We want the node item in the tuple (fScore, nodeHash)
		currentNodeHash = heappop(heap)[1]
		# Get the node from the dictionary
		currentNode = nodes[currentNodeHash]

		# Visualize all closed nodes
		board.setClosedNode(map, currentNode)

		if currentNode == goalNode: # Win!
			board.createShortestPath(map, currentNode)
			break

		# Go through all neighbors
		for child in findChildren(map, currentNode, nodes):
			hash = child.hash()
			# Set the total node cost
			child.setNodeCost(map)

			# Dijkstra is a special case of A* where the heuristic function
			# returns 0
			# Calculate f()
			fScore = child.cost

			# Add score and node hash to the heap
			heappush(heap, (fScore, hash))

			# Keep the discovered node
			nodes[hash] = child

			# Visualize all open nodes
			board.setOpenNode(map, child)

	numberOfOpenedNodes = len(nodes)
	return map, numberOfOpenedNodes, numberOfClosedNodes