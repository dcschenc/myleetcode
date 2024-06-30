class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[float(inf) for j in range(n)] for i in range(m)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i-1][j] + matrix[i][j])
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + matrix[i][j])
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], dp[i-1][j + 1] + matrix[i][j])
        # print(dp)
        return min(dp[m-1])