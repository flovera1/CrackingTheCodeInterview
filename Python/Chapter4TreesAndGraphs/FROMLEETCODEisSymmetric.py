'''
Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric


    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not.

    1
   / \
  2   2
   \   \
   3    3
'''
class TreeNode:
    def __init__(self, x, valLeft = None, valRight = None):
        self.val = x
        self.vLeft = valLeft
        self.vRight = valRight
        self.vIsVisited = False

    def __str__(self):
        print(str(self.val) +' hijo izq: '+ str(self.vLeft.val) + ' hijo derecho: '+ str(self.vRight.val))
        return ""

    def sym(self,left,right):
        if left==None and right==None:
            return True
        if left and right and left.val == right.val:
            return self.sym(left.left,right.left) and self.sym(left.right, right.right)
        else:
            return False
                
    def isSymmetric(self, root):
        if root==None:
            return True
        return self.sym(root.left,root.right)        

