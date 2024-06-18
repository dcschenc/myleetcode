class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m, n = len(grid), len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if grid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j-1] if j > 0 else 1
                elif j == 0:
                    if grid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i-1][j] if i > 0 else 1
                else:
                    if grid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
