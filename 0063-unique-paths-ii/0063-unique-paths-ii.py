class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= m or j >= n or obstacleGrid[i][j]:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            return dfs(i + 1, j) + dfs(i, j + 1)

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return dfs(0, 0)
        
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
