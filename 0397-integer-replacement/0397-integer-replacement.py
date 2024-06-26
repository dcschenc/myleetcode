class Solution:
    def integerReplacement(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 1:
                return 0
            if i % 2 == 0:
                return 1 + dp(i // 2)
            else:
                return 1 + min(dp(i + 1), dp(i - 1))
        
        return dp(n)