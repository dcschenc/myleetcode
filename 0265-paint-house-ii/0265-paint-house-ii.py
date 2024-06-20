class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        dp = [[0 for j in range(k)] for i in range(n)]
        for j in range(k):
            dp[0][j] = costs[0][j]
        for i in range(1, n):
            for j in range(k):
                dp[i][j] = min([dp[i-1][m] + costs[i][j] for m in range(k) if m != j])
        return min(dp[n-1])