class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = matrix.copy()
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            mx = max(matrix[i][j] for i in range(m))
            for i in range(m):
                if ans[i][j] == -1:
                    ans[i][j] = mx
        return ans