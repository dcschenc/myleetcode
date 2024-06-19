class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        buy = [-prices[0]] * k
        sell = [0] * k      

        for i in range(len(prices)):
            for j in range(k):
                buy[j] = max(buy[j], (sell[j-1] - prices[i]) if j > 0 else -prices[i])
                sell[j] = max(sell[j], buy[j] + prices[i])
        return sell[k-1]
        

        # If k is greater than half the number of days, you can perform as many transactions as you want.
        # if k >= n // 2:
        #     return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1)

        # dp = [[0] * (k + 1) for _ in range(n)]

        # for j in range(1, k + 1):
        #     max_diff = -prices[0]
        #     for i in range(1, n):
        #         dp[i][j] = max(dp[i - 1][j], prices[i] + max_diff)
        #         max_diff = max(max_diff, dp[i][j - 1] - prices[i])

        # return dp[n - 1][k]