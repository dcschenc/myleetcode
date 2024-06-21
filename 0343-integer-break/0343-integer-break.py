class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        dp = [0] * (n + 1)

        # Set base cases
        for i in [1, 2, 3]:
            dp[i] = i
            
        for num in range(4, n + 1):
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp[num - i])
            
            dp[num] = ans
        
        return dp[n]
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        # dp[2] = 1

        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * (i - j), j * (i - j))
        # print(dp)
        return dp[n]
