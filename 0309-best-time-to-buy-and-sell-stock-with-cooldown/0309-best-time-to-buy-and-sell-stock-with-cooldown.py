class Solution:
    def maxProfit(self, prices: List[int]) -> int:     
        
#         @cache
#         def dp(i, holding):
#             if i >= len(prices):
#                 return 0
#             do_nothing = dp(i + 1, holding)
            
#             do_something = 0
#             if holding:
#                 do_something =  prices[i] + dp(i + 2, 0)
#             else:
#                 do_something = -prices[i] + dp(i + 1, 1)
                
#             return max(do_nothing, do_something)
            
#         return dp(0, 0)

        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        for i in range(n-1, -1, -1):
            for holding in range(2):
                do_nothing = dp[i + 1][holding]
                do_something = 0
                if holding:
                    if i + 2 > n:
                        do_something = prices[i]
                    else:
                        do_something = prices[i] + dp[i + 2][0]
                else:
                    do_something = - prices[i] + dp[i + 1][1]
                dp[i][holding] = max(do_something, do_nothing)
        return dp[0][0]
        
        
        if not prices:
            return 0

        n = len(prices)
        buy = [0] * n
        sell = [0] * n

        buy[0] = -prices[0]

        for i in range(1, n):
            # Calculate the maximum profit on each day considering buying or not buying
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

        return max(sell[n - 1], buy[n - 1])