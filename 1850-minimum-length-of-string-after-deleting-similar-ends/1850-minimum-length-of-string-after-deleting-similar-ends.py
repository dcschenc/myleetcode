class Solution:
    def minimumLength(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1750.Minimum%20Length%20of%20String%20After%20Deleting%20Similar%20Ends
        if len(s) == 1:
            return 1
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            if s[i] != s[j]:
                return j - i + 1
            while i + 1 < j and s[i+1] == s[i]:
                i += 1
            i += 1
            while j - 1 > i and s[j-1] == s[j]:
                j -= 1
            j -= 1
            if i > j:
                return 0
            if i == j:
                return 1
        