'''
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
def searchWord(grid, word):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if (dfs(grid, word, i, j)):
				return True 

	return False 


def dfs(grid, word, i, j):
	if len(word) == 0:
		return True

	if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] != word[0]:
		return False

	temp = grid[i][j]
	grid[i][j] = '' #to don't come back to it.

	result = dfs(grid, word[1:], i+1, j) or dfs(grid, word[1:], i-1, j) or dfs(grid, word[1:], i, j+1) or dfs(grid, word[1:], i, j-1) 

	grid[i][j] = temp #restore the board.

	return result


board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]

print(searchWord(board, "ABCCED"))