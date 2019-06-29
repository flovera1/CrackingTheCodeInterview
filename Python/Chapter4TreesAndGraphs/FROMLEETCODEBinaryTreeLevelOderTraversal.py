'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

	3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

'''
class TreeNode:
	def __init__(self, valValue, valLeft=None, valRight=None):
		self.vValue = valValue
		self.vLeft = valLeft
		self.vRight = valRight


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





root2 = TreeNode(9)
root4 = TreeNode(15)
root5 = TreeNode(7)

root3 = TreeNode(20, root4, root5)

root = TreeNode(3, root2, root3)





result = listOfLevels(root)

print result

