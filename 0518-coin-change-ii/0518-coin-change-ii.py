class Solution:    
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for j in range(n + 1)] for i in range(amount + 1)]
        
        # Base case: there is one way to make amount 0, which is by not selecting any coin.
        for j in range(n + 1):
            dp[0][j] = 1  

        for i in range(1, amount + 1):
            for j in range(1, n + 1):
                # Ways without using the current coin
                dp[i][j] += dp[i][j - 1]

                if i - coins[j - 1] >= 0:
                    # Ways using the current coin
                    dp[i][j] += dp[i - coins[j - 1]][j]

        return dp[amount][n]
    
    
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]


        # @cache
        # def backtrack(target, startIdx):
        #     # nonlocal count
        #     # nonlocal path
        #     count = 0
        #     if target == 0:
        #         count = 1
        #         return count

        #     for i in range(startIdx, len(coins)):
        #         if coins[i] > target:
        #             break
        #         else:
        #             target = target - coins[i]
        #             # path.append(coins[i])
        #             count += backtrack(target, i)
        #             target = target + coins[i]
        #             # path.pop()
            
        #     return count
        
        # # count = 0
        # # path = []
        # coins.sort()        
        # count = backtrack(amount, 0)
        # return count


