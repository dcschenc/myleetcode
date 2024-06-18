class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return dp[n - 1]
    
    
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]  # 0: buy, 1: sell
        dp[0][1] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return dp[-1][1]

        max_profit = 0
        left = prices[0]
        for i in range(1, len(prices)):
            # max_profit = max(max_profit, prices[i] - left)
            # left = min(left, prices[i])
            if prices[i] - left > max_profit:
                max_profit = prices[i] - left
            if prices[i] < left:
                left = prices[i]
        return max_profit

        if not prices:
            return 0

