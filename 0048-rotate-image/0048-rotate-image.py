class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # print(m,n)
        for i in range(m):
            for j in range(i, n):
                # print(i, j)
                # tmp = matrix[i][j]
                # matrix[i][j] = matrix[j][i]
                # matrix[j][i] = tmp
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # print(matrix)
        for i in range(m):
            matrix[i].reverse()
        