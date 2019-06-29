'''
Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
'''
class Node:
	def __init__(self, valValue, valRightChildren=None, valLeftChildren=None):
		self.vValue = valValue
		self.vRightChildren = valRightChildren # they is supposed to be a list of nodes.
		self.vLeftChildren = valLeftChildren # they is supposed to be a list of nodes.

	def __str__(self):
		return '('+str(self.vLeftChildren)+':L ' + "V:" + str(self.vValue) + " R:" + str(self.vRightChildren)+')'

def createBinaryTree(valArrayOfSortedNumbers):

	if valArrayOfSortedNumbers==[]:
		return Node(valArrayOfSortedNumbers)

	vMidIndex = len(valArrayOfSortedNumbers)/2
	vRootNode = Node(valArrayOfSortedNumbers[vMidIndex])
	vRootNode.vLeftChildren = createBinaryTree(valArrayOfSortedNumbers[vMidIndex+1:])
	vRootNode.vRightChildren = createBinaryTree(valArrayOfSortedNumbers[:vMidIndex]) 
	
	return vRootNode



print(createBinaryTree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]))