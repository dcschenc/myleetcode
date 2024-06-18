class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row_0 = set()
        col_0 = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_0.add(i)
                    col_0.add(j)
        for i in row_0:
            for k in range(n):
                matrix[i][k] = 0
        for j in col_0:
            for q in range(m):
                matrix[q][j] = 0

        # res = []
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             res.append((i,j))
        # for i, j in res:
        #     for k in range(n):
        #         matrix[i][k] = 0
        #     for q in range(m):
        #         matrix[q][j] = 0
        