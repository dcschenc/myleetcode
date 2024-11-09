class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2596.Check%20Knight%20Tour%20Configuration
        if grid[0][0]:
            return False
        n = len(grid)
        pos = [None] * (n * n)
        for i in range(n):
            for j in range(n):
                pos[grid[i][j]] = (i, j)
        for (x1, y1), (x2, y2) in pairwise(pos):
            dx, dy = abs(x1 - x2), abs(y1 - y2)
            ok = (dx == 1 and dy == 2) or (dx == 2 and dy == 1)
            if not ok:
                return False
        return True

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
        