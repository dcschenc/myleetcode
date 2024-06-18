class Solution:
    # hm = {}
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        # if n in self.hm:
            # return self.hm[n]
        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # self.hm[n] = res
        return res

        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]