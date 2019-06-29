'''
Implement a function to check if a binary tree is balanced. A balanced tree is 
supposed to be a tree such that the heights of the subtrees of any node never
differ by more than 1.

	3
   / \
  9  20
    /  \
   15   7


'''

class TreeNode:
	def __init__(self, valValue = None, valLeft = None, valRight = None):
		self.vValue = valValue
		self.vLeft = valLeft
		self.vRight = valRight

def heightOfATreeNode(valTreeNode):
	if valTreeNode == None:
		return 0

	vResult = 1

	#vValue = valTreeNode.vValue
	vLeftNode = valTreeNode.vLeft
	vRightNode = valTreeNode.vRight

	vResult += heightOfATreeNode(vLeftNode) + heightOfATreeNode(vRightNode)

	return vResult


def checkBalance(valTreeNode):
	if valTreeNode == None:
		return True


	if (valTreeNode!=None):
		vLeftNode = valTreeNode.vLeft
		vRightNode = valTreeNode.vRight

		vHeightLeft = heightOfATreeNode(vLeftNode)
		vHeightRight = heightOfATreeNode(vRightNode)

		if (abs(vHeightLeft - vHeightRight) > 1):
			return False

		return checkBalance(vLeftNode) and checkBalance(vRightNode)



root2 = TreeNode(9)
root4 = TreeNode(15)
root5 = TreeNode(7)

root3 = TreeNode(20, None, None)

root = TreeNode(3, root2, root3)



print(checkBalance(root))