'''
Find the sum of all leaves in a given binary tree
'''


class TreeNode:
	def __init__(self, valValue, vLeft=None, vRight=None):
		self.vValue = valValue
		self.vLeft = vLeft
		self.vRight = vRight

def sumLeaves(valRoot):
	vResult = 0

	vRightBranch = valRoot.vRight
	if valRoot.vLeft == None and valRoot.vRight == None:
		vResult += valRoot.vValue

	if valRoot.vLeft != None:
		vResult += sumLeaves(valRoot.vLeft)

	if vRightBranch != None:
		if vRightBranch.vLeft != None:
			vResult += sumLeaves(vRightBranch.vLeft)

	return vResult

vTreeNode1 = TreeNode(9)
vTreeNode2 = TreeNode(15)
vTreeNode3 = TreeNode(7)

vTreeNode4 = TreeNode(20, vTreeNode2, vTreeNode3)
vTreeNode5 = TreeNode(3, vTreeNode1, vTreeNode4)

print(sumLeaves(vTreeNode5))



