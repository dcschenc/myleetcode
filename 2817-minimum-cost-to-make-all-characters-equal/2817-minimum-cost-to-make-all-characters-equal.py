class Solution:
    def minimumCost(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2712.Minimum%20Cost%20to%20Make%20All%20Characters%20Equal
        ans, n = 0, len(s)
        for i in range(1, n):
            if s[i] != s[i - 1]:
                ans += min(i, n - i)
        return ans