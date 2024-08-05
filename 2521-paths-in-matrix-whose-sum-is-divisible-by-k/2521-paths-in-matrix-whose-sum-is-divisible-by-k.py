class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        # @cache
        # def dfs(i, j, s):
        #     if i < 0 or i >= m or j < 0 or j >= n:
        #         return 0
        #     s = (s + grid[i][j]) % k
        #     if i == m - 1 and j == n - 1:
        #         return int(s == 0)
        #     ans = dfs(i + 1, j, s) + dfs(i, j + 1, s)
        #     return ans % mod

        # m, n = len(grid), len(grid[0])
        # mod = 10**9 + 7
        # ans = dfs(0, 0, 0)
        # dfs.cache_clear()
        # return ans

        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2435.Paths%20in%20Matrix%20Whose%20Sum%20Is%20Divisible%20by%20K
        @cache
        def dfs(i, j, s):
            if i >= m or j >= n:
                return 0
            s = (s + grid[i][j]) % k
            if i == m - 1 and j == n - 1:
                return int(s % k == 0) 
            ans = 0           
            ans += dfs(i + 1, j, s)
            ans += dfs(i, j + 1, s)
            return ans % mod

        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7
        ans = dfs(0, 0, 0) % mod
        dfs.cache_clear()
        return ans
        