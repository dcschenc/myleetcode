class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(r, c):
            x = y = z = 0
            if 0 <= r - 1 <= m - 1 and 0 <= c + 1 <= n - 1 and grid[r][c] < grid[r-1][c+1]:
                x = dfs(r - 1, c + 1)
            if 0 <= r <= m - 1 and 0 <= c + 1 <= n - 1 and grid[r][c] < grid[r][c+1]:
                y = dfs(r, c + 1)
            if 0 <= r + 1 <= m - 1 and 0 <= c + 1 <= n - 1 and grid[r][c] < grid[r+1][c+1]:
                z = dfs(r + 1, c + 1)
            return 1 + max(x, y, z) 

        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            ans = max(ans, dfs(i, 0))
        return ans - 1
