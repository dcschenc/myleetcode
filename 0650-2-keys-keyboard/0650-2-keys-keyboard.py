class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dp(i, cur, steps):
            if i == n:
                return steps
            if i > n:
                return float('inf')
            if cur != 0:
                steps = min(dp(i + i, i, steps + 2), dp(i + cur, cur, steps + 1))
            else:
                steps = dp(i + i, i, steps + 2)
            return steps
        
        steps = dp(1, 0, 0)
        return steps
        