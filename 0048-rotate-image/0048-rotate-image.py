class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # https://github.com/doocs/leetcode/tree/main/solution/0000-0099/0048.Rotate%20Image
        m, n = len(matrix), len(matrix[0])
        # print(m,n)
        for i in range(m):
            for j in range(i, n):     
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(m):
            matrix[i].reverse()
        