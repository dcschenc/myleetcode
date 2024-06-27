class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:        
        if not prices: return 0

        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)
        return dp[n-1][1]

        # # Create two lists to track the best time to buy (buy) and sell (sell) at each day.
        # buy = [0] * n
        # sell = [0] * n

        # # Initialize the first day's "buy" value.
        # buy[0] = -prices[0]

        # for i in range(1, n):
        #     # Calculate the next "buy" and "sell" values based on the previous day's values.
        #     buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])
        #     sell[i] = max(sell[i - 1], buy[i - 1] + prices[i] - fee)

        # # The maximum profit is obtained on the last day by selling.
        # return max(sell[n - 1], buy[n-1])
