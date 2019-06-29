'''
Given a binary tree, design an algorithm which creates a linked list of all nodes at
each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
'''

class TreeNode:
	def __init__(self, valValue, valLeft=None, valRight=None):
		self.vValue = valValue
		self.vLeft = valLeft
		self.vRight = valRight
		self.vIsVisited = False


def listOfLevels(root):
	if root==None:
		return []

	vReturnList = []
	vQueue = [root]
	while(len(vQueue) > 0):
		vReturnList.append([node.vValue for node in vQueue])
		newNodes = []

		for node in vQueue:
			if node.vLeft:
				newNodes.append(node.vLeft)
			if node.vRight:
				newNodes.append(node.vRight)
		vQueue = newNodes

	return vReturnList

def listOfLevels2(root):
	vQueue = [root]
	vResult = [[root.vValue]]

	while(vQueue):
		vElement = vQueue.pop()
		vElement.vIsVisited = True
		vAdjancents = [vElement.vLeft, vElement.vRight]
		vListPerLevel = []
		# for per level
		for node in vAdjancents:
			if node != None and not(node.vIsVisited):
				vListPerLevel.append(node.vValue)
				vQueue.append(node)

		if(vListPerLevel != []):
			vResult.insert(0, vListPerLevel)

	return vResult

root2 = TreeNode(9)
root4 = TreeNode(15)
root5 = TreeNode(7)

root3 = TreeNode(20, root4, root5)

root = TreeNode(3, root2, root3)





result = listOfLevels2(root)

print result















