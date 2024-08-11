class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2742.Painting%20the%20Walls
        @cache
        def dp(i, j):
            if n - i <= j:
                return 0
            if i >= n:
                return float('inf')
            return min(dp(i + 1, j + time[i]) + cost[i], dp(i + 1, j - 1))
        n = len(cost)
        return dp(0, 0)

        # n = len(cost)
        # dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # for i in range(1, n + 1):
        #     dp[n][i] = inf

        # for i in range(n - 1, -1, -1):
        #     for remain in range(1, n + 1):
        #         paint = cost[i] + dp[i + 1][max(0, remain - 1 - time[i])]
        #         dont_paint = dp[i + 1][remain]
        #         dp[i][remain] = min(paint, dont_paint)
        
        # return dp[0][n]