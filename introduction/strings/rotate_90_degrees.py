from copy import deepcopy
def rotateMatrix(matrix, n):
    res = deepcopy(matrix) 
    for x in range(0, n):
        for y in range(n-1, -1, -1):
            res[x][n-y-1] = matrix[y][x]
    return res

n = 3

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("original matrix "+ str(matrix))
print("rotated matrix "+str(rotateMatrix(matrix, n)))