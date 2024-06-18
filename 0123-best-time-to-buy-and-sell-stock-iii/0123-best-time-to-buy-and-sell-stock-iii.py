class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy = [-prices[0]] * 2
        sell = [0] * 2
        for i in range(len(prices)):
            for j in range(2):
                buy[j] = max(buy[j], (sell[j-1] - prices[i]) if j > 0 else -prices[i])
                sell[j] = max(sell[j], buy[j] + prices[i])
            # buy[0] = max(buy[0], -prices[i])
            # sell[0] = max(sell[0], buy[0] + prices[i])
            # buy[1] = max(buy[1], sell[0] - prices[i])
            # sell[1] = max(sell[1], buy[1] + prices[i])
        return sell[1]

        # if not prices:
        #     return 0
        
        # n = len(prices)
        # # Store the best buying options for the first and second transactions
        # buy = [-prices[0]] * 2  
        # # Store the best selling options for the first and second transactions
        # sell = [0] * 2        
        
        # for i in range(1, n):
        #     # Update the best buying option for the first transaction
        #     buy[0] = max(buy[0], -prices[i]) 
        #     # Update the best selling option for the first transaction
        #     sell[0] = max(sell[0], buy[0] + prices[i]) 
        #     # Update the best buying option for the second transaction
        #     buy[1] = max(buy[1], sell[0] - prices[i]) 
        #     # Update the best selling option for the second transaction
        #     sell[1] = max(sell[1], buy[1] + prices[i]) 
        
        # return sell[1] 
