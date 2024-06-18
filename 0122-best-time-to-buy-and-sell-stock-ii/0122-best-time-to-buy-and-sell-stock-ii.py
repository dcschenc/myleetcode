class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i-1]:
        #         max_profit += prices[i] - prices[i-1]
        # return max_profit


        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return dp[n-1][1]

        # dp = [0] * n

        # for i in range(1, n):
        #     if prices[i] > prices[i - 1]:
        #         dp[i] = dp[i - 1] + prices[i] - prices[i - 1]
        #     else:
        #         dp[i] = dp[i - 1]

        # return dp[n - 1]