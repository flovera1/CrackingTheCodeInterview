'''
Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
'''
class Node:
	def __init__(self, valValue, valAdjacentLength, valAdjancentList):
		self.vVertex = valValue
		self.vAdjacencyLength = valAdjacentLength
		self.vAdjacent = valAdjancentList
		self.vVisited = False

	def addAdjacent(self, valNode):
		self.vAdjacent.append(valNode)
		self.vAdjacencyLength += 1

	def getAdjacent(self):
		return self.vAdjacent

	def getVertex(self):
		return self.vVertex

	def __str__(self):
		print("Vertex value: ")
		print(self.vVertex)
		print("---------------------------")
		print("And its adjacent list:")
		for i in self.vAdjacent:
			print(i)
		return ""
		

class Graph:
	def __init__(self, valNumberOfNodes):
		self.vNumberOfNodes = valNumberOfNodes
		self.vListOfNodes = []
	
	def addNode(self, valNode):
		self.vNumberOfNodes += 1
		self.vListOfNodes.append(valNode)

	def getListOfNodes(self):
		return self.vListOfNodes

	def getNumberOfNodes(self):
		return self.vNumberOfNodes


def isPathBFS(valGraph, valNode1, valNode2): #method that determines if there's a path betwee two nodes
	valNode1.vVisited = True
	vQueue = [valNode1]
	vVisitedNodes = []
	while len(vQueue) > 0:
		vTempNode = vQueue.pop()
		vAdjancentList = vTempNode.vAdjacent
		
		for node in vAdjancentList:
			if node == valNode2.vVertex:
				return True
		print(vTempNode.vAdjacent)
		
	return False



vGraph = Graph(5)
valListOfNodes = [0]*5
valListOfNodes[0] = Node("b", 2, ["a", "c"])
valListOfNodes[1] = Node("c", 0, [])
valListOfNodes[2] = Node("d", 2, ["f", "e"])
valListOfNodes[3] = Node("e", 0, [])
valListOfNodes[4] = Node("f", 0, [])

vGraph.addNode(valListOfNodes[0])
vGraph.addNode(valListOfNodes[1])
vGraph.addNode(valListOfNodes[2])
vGraph.addNode(valListOfNodes[3])
vGraph.addNode(valListOfNodes[4])

# is there a path or no?
print(isPathBFS(vGraph, valListOfNodes[0], valListOfNodes[1]))