class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n+1):  # i == 1, s[0]          
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i > 1 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] = dp[i] + dp[i-2]
        return dp[n]
            
        @cache
        def backtrack(idx):
            # if idx in memo:
            #     return memo[idx]           
            if idx == len(s):
                return 1
            ways = 0            
            if 1 <= int(s[idx]) <= 9:
                ways += backtrack(idx + 1)
            if 10 <= int(s[idx:idx + 2]) <= 26:
                ways += backtrack(idx + 2)            
            # memo[idx] = ways
            return ways
            
        memo = {}
       
        ways = backtrack(0)
        return ways