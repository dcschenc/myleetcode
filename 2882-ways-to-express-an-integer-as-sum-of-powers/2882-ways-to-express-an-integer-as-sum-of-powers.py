class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10 ** 9 + 7      
        # Initializing a dynamic programming table where
        # dp[i][j] represents the number of ways to write j as a sum
        # of i-th powers of first i natural numbers.
        dp = [[0] * (n + 1) for _ in range(n + 1)]
      
        # There is one way to form the sum 0 using 0 numbers: use no numbers at all.
        dp[0][0] = 1
      
        # Iterate over all numbers from 1 to total_sum
        for i in range(1, n + 1):
            # Calculate the i-nth power of the number
            power = pow(i, x)
            # Iterate over all possible sums from 0 to total_sum
            for j in range(n + 1):
                # The number of ways to form the sum j without using the i-th number
                dp[i][j] = dp[i - 1][j]
                # If the power is less than or equal to the sum j, then
                # add the number of ways to form the previous sum j-power
                if power <= j:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - power]) % mod
      
        # Return the number of ways to write total_sum as a sum of
        # powers of the first total_sum natural numbers.
        return dp[n][n]


        # @cache
        # def backtrack(i, cur):
        #     if cur == n:                
        #         return 1            
        #     ans = 0
        #     for j in range(i, len(candidates)):  
        #         if cur + candidates[j] > n:
        #             break              
        #         ans += backtrack(j + 1, cur + candidates[j])
        #         ans = ans % (10 ** 9 + 7)
        #     return ans

        # candidates = []
        # i = 1
        # while i <= n:
        #     if i ** x <= n:
        #         candidates.append(i ** x)
        #         i += 1
        #     else:
        #         break
        # candidates.sort()
        # ans = backtrack(0, 0)
        # return ans % (10 ** 9 + 7)