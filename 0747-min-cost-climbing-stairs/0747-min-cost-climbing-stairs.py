class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:    
        n = len(cost)
        f = [0] * (n + 1)
        for i in range(2, n + 1):
            f[i] = min(f[i - 2] + cost[i - 2], f[i - 1] + cost[i - 1])
        return f[n]
    
        n = len(cost)
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            if i == n-1:
                dp[i] = min(dp[i-1], dp[i-2] + cost[i])
            else:
                dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        # print(dp)
        return dp[n-1]
        