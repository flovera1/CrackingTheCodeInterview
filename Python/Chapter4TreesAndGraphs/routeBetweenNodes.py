'''
Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
''' 

# We need to represent a Graph. This will be done with a matrix
class Graph:
	def __init__(self, valMatrix):
		self.vMatrix = valMatrix

	def get_adj(self, valNode):
		vResult = []
		for i, val in enumerate(self.vMatrix[valNode]):
			if val == 1:
				vResult.append(i)

		return vResult

	def length_of_matrix(self):
		return len(self.vMatrix)

def hasPath(valGraph, valNode1, valNode2):
	vQueue = [valNode1]
	vVisited = []
	while(len(vQueue) > 0):
		vElementOfQueue = vQueue.pop() # dequeue
		vAdjancecyList = valGraph.get_adj(vElementOfQueue)

		if(vElementOfQueue == valNode2):
			return True

		if not(vElementOfQueue in vVisited and vElementOfQueue in vAdjancecyList):
			vVisited.append(vElementOfQueue)

	return False




vMatrix = 	[[1,0,0,1], 
		     [0,1,1,1],
             [0,1,1,0],
             [0,0,1,1]]

vGrapg = Graph(vMatrix)
print(hasPath(vGrapg,0,2))
'''
assert (hasPath(vGrapg,0,2))
assert (hasPath(vGrapg,0,1))
assert (hasPath(vGrapg,2,3))
assert (hasPath(vGrapg,2,0)==False)
assert (hasPath(vGrapg,1,0)==False)
'''
print(hasPath(vGrapg,0,0))