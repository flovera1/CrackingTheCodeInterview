class TreeNode:
    def __init__(self, valValue, valLeft=None, valRight=None):
        self.vValue = valValue
        self.vLeft = valLeft
        self.vRight = valRight
        self.vIsVisited = False

def averageNodesBFS(valRoot):
    vQueue = [valRoot]
    vResult = []
    vResult.append(valRoot.vValue*1.0) # append of the rootnode
    while(vQueue):
        vElement = vQueue.pop()
        vElement.vIsVisited = True
        vListAdj = [vElement.vLeft, vElement.vRight]
        
        vSumLevel = 0
        vCountNodes = 0
        vAverage = 0
        # This for is for level.
        for node in vListAdj:
            vCountNodes += 1
            if node != None and not(node.vIsVisited):
                vSumLevel += node.vValue
                #print(node.vValue)
                vQueue.append(node)

        if vSumLevel != 0:
            vResult.append(vSumLevel*1.0/vCountNodes)
           




    return vResult






root2 = TreeNode(9)
root4 = TreeNode(15)
root5 = TreeNode(7)

root3 = TreeNode(20, root4, root5)

root = TreeNode(3, root2, root3)





result = averageNodesBFS(root)

print result

