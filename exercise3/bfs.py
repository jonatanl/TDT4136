from Queue import Queue
from heapq import heappush, heappop, heapify
import board
from node import Node
from util import *

def bfs(map, startNode, goalNode):
	# Using a queue to keep track of the next node to visit.
	# This is a FIFO queue
	queue = Queue()

	# Generate value to hash
	hash = startNode.hash()

	# Min heap with fScore as the value. heap only contains open nodes
	queue.put(hash)

	# All open and closed nodes is in the dictionary
	nodes = {startNode.hash(): startNode}

	# Count the total number of closed nodes
	numberOfClosedNodes = 0

	# Run while there still exist opened nodes
	while queue.qsize() > 0:
		numberOfClosedNodes += 1

		# We want the node item in the tuple (fScore, nodeHash)
		currentNodeHash = queue.get()
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
			# Add child to queue
			queue.put(hash)

			# Keep the discovered node
			nodes[hash] = child

			# Visualize all open nodes
			board.setOpenNode(map, child)

	numberOfOpenedNodes = len(nodes)
	return map, numberOfOpenedNodes, numberOfClosedNodes