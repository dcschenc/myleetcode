class Solution:
    def findDerangement(self, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0600-0699/0634.Find%20the%20Derangement%20of%20An%20Array
        a, b = 1, 0
        mod = 10 ** 9 + 7
        for i in range(2, n + 1):
            c = (i-1) * (a + b) % mod
            a = b
            b = c
        ans = b % mod
        return ans

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = (i-1) * dp[i-1] + (i-1) * dp[i-2]
        ans = dp[-1] % (10 ** 9 + 7)
        return ans
