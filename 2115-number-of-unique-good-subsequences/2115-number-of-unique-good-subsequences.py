class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1987.Number%20of%20Unique%20Good%20Subsequences
        f = g = 0
        ans = 0
        mod = 10**9 + 7
        for c in binary:
            if c == "0":
                g = (g + f) % mod
                ans = 1
            else:
                f = (f + g + 1) % mod
        ans = (ans + f + g) % mod
        return ans