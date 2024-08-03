class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2304.Minimum%20Path%20Cost%20in%20a%20Grid
        m, n = len(grid), len(grid[0])
        dp = [[float('inf') for j in range(n)] for i in range(m)]
        for j in range(n):
            dp[0][j] = grid[0][j]
        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + moveCost[grid[i-1][k]][j] + grid[i][j])

        return min(dp[m-1])