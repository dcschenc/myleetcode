class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2596.Check%20Knight%20Tour%20Configuration
        def dfs(x, y, idx):
            if idx == m * n:
                return True
            for dx, dy in [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1:
                    if grid[new_x][new_y] == idx:
                        if dfs(new_x, new_y, idx + 1):
                            return True
            return False

        m, n = len(grid), len(grid[0])
        if grid[0][0] != 0:
            return False
        return dfs(0, 0, 1)
        