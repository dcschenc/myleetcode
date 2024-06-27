class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if 0<=i-1<=m-1 and 0<=j-1<=n-1 and matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True 
