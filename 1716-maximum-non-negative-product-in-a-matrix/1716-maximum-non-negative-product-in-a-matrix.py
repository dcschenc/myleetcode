class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1594.Maximum%20Non%20Negative%20Product%20in%20a%20Matrix
        mod = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[float('inf'), -float('inf')] for j in range(n)] for i in range(m)] 
        dp[0][0][0] = dp[0][0][1] = grid[0][0]
        for j in range(1, n):
            dp[0][j][0] = dp[0][j][1] = dp[0][j-1][0] * grid[0][j]
        for i in range(1, m):
            dp[i][0][0] = dp[i][0][1] =  dp[i-1][0][0] * grid[i][0]

        for i in range(1, m):
            for j in range(1, n):                
                cur = grid[i][j]
                choices = [dp[i-1][j][0] * cur, dp[i-1][j][1] * cur, dp[i][j-1][0] * cur, dp[i][j-1][1] * cur]
                dp[i][j][0] = max(choices)
                dp[i][j][1] = min(choices)
        # print(dp)
        return dp[m-1][n-1][0] % mod if dp[m-1][n-1][0] >= 0 else -1