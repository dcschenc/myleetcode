class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        mod = 10**9 + 7
        dp = [1] + [0] * maxLength
        for i in range(1, len(dp)):
            if i - oneGroup >= 0:
                dp[i] += dp[i - oneGroup]
            if i - zeroGroup >= 0:
                dp[i] += dp[i - zeroGroup]
            dp[i] %= mod
        return sum(dp[minLength:]) % mod