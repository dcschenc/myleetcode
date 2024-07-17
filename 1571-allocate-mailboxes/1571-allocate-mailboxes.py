class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1478.Allocate%20Mailboxes
        houses.sort()
        n = len(houses)        
        # Precompute costs for placing a mailbox between houses[i:j+1]
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                mid = (i + j) // 2
                for l in range(i, j + 1):
                    cost[i][j] += abs(houses[l] - houses[mid])

        # Initialize DP array
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(i):
                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p][i - 1])
        
        return dp[n][k]

        houses.sort()
        n = len(houses)
        g = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = g[i + 1][j - 1] + houses[j] - houses[i]
        f = [[inf] * (k + 1) for _ in range(n)]
        for i in range(n):
            f[i][1] = g[0][i]
            for j in range(2, min(k + 1, i + 2)):
                for p in range(i):
                    f[i][j] = min(f[i][j], f[p][j - 1] + g[p + 1][i])
        return f[-1][k]