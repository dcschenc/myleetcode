class Solution:
    def maxA(self, n: int) -> int:
        @cache
        def dp(i, cur, steps):
            if steps == n:
                return i
            if steps > n:
                return -float('inf')
            if cur == 0:
                ans = max(dp(i + i, i, steps + 3), dp(i + 1, cur, steps + 1))
            else:
                ans = max(dp(i + cur, cur, steps + 1), dp(i + i, i, steps + 3))
            return ans

        ans = dp(1, 0, 1)
        return ans
        