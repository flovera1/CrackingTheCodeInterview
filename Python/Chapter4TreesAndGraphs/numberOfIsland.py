'''
Given a 2d grid map of '1's (land) and '0's (water), vCount the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''
def traverseThevalGraph(valGraph): 
	vRows = len(valGraph)
	vCols = len(valGraph)
	vCount = 0
	for i in range(vRows):
		for j in range(vCols):
			if valGraph[i][j] == 1:
				dfs(valGraph, vRows, vCols, i, j)
				vCount += 1

	return vCount


def dfs(valGraph, valRows, valCols, valX, valY):
	if(valGraph[valX][valY] == 0):
		return

	valGraph[valX][valY] = 0

	if(valX != 0):
		dfs(valGraph, valRows, valCols, valX-1, valY)
	if(valX != valRows-1):
		dfs(valGraph, valRows, valCols, valX+1, valY)

	if(valY != 0):
		dfs(valGraph, valRows, valCols, valX, valY-1)
	if(valY != valCols-1):
		dfs(valGraph, valRows, valCols, valX, valY+1)



vMatrix = 	[[1,0,0,1], 
		     [0,1,1,1],
             [0,1,1,0],
             [0,0,1,1]]

print(traverseThevalGraph(vMatrix))