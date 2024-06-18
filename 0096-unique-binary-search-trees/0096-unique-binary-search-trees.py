class Solution:
    def numTrees(self, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0000-0099/0096.Unique%20Binary%20Search%20Trees
        dp = [0] * (n + 1)        
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[-1]