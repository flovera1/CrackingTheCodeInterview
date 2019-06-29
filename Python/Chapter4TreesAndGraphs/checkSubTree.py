'''
T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
algorith m to determine if T2 is a subtree of T1 .
A tree T2 is a subtree ofTi if there exists a node n in Ti such that the subtree of 
n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
'''
class TreeNode:
	def __init__(self, valValue=None, valLeft=None, valRight=None):
		self.vValue = valValue
		self.vLeft = valLeft
		self.vRight = valRight

def subtree(valTreeNode1, valTreeNode2):
	if valTreeNode2 == None:
		return True
	if valTreeNode1 == None:
		return False

	if (identical(valTreeNode1, valTreeNode2)):
		return True
	return subtree(valTreeNode1.vLeft, valTreeNode2) or subtree(valTreeNode1.vRight, valTreeNode2)

def identical(valNodeTree1, valNodeTree2):
	if valNodeTree1== None and valNodeTree2==None:
		return True
	if valNodeTree1.vValue != valNodeTree2.vValue:
		return False
	return identical(valNodeTree1.vLeft, valNodeTree2.vLeft) and identical(valNodeTree1.vRight, valNodeTree2.vRight)




root2 = TreeNode(9)
root4 = TreeNode(5000)
root5 = TreeNode(7)

root3 = TreeNode(20, root4, root5)

root = TreeNode(3, root2, root3)

print(subtree(root, root3))