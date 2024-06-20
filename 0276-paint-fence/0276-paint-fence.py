class Solution:
    def numWays(self, n: int, k: int) -> int:
        # dp = [[0 for j in range(2)] for i in range(n)]
        # dp[0][0] = k        
        # for i in range(1, n):
        #     dp[i][0] = (dp[i-1][0] + dp[i-1][1]) * (k - 1)
        #     dp[i][1] = dp[i-1][0]
        # return sum(dp[-1])

        @lru_cache(None)
        def total_ways(i):
            if i == 1: 
                return k
            if i == 2: 
                return k * k
            
            return (k - 1) * (total_ways(i - 1) + total_ways(i - 2))
        
        return total_ways(n)