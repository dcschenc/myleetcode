class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        res = [[-1 for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                num = i * c + j
                x = num // n
                y = num % n
                res[i][j] = mat[x][y]
        return res