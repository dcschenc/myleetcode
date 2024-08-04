class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        @cache
        def dfs(i, j):
            if j > k:
                return 0
            if j == k:
                if i == endPos:
                    return 1
                return 0
            ans = 0
            ans += dfs(i + 1, j + 1)
            ans += dfs(i - 1, j + 1)
            return ans
        mod = 10 ** 9 + 7
        return dfs(startPos, 0) % mod
        