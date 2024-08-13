class Solution:
    def minChanges(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2914.Minimum%20Number%20of%20Changes%20to%20Make%20Binary%20String%20Beautiful
        i, n = 0, len(s)
        total = 0
        while i < n - 1:
            if s[i] != s[i+1]:
                total += 1
            i += 2
        return total