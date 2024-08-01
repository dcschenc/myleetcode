class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2209.Minimum%20White%20Tiles%20After%20Covering%20With%20Carpets
        @cache
        def dfs(i, j):
            if i >= n:
                return 0
            if floor[i] == '0':
                return dfs(i + 1, j)
            if j == 0:
                return s[-1] - s[i]
            return min(1 + dfs(i + 1, j), dfs(i + carpetLen, j - 1))

        n = len(floor)
        s = [0] * (n + 1)
        for i, c in enumerate(floor):
            s[i + 1] = s[i] + int(c == '1')
        ans = dfs(0, numCarpets)
        dfs.cache_clear()
        return ans