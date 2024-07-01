class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def backtrack(x, y, cnt):
            if cnt == total:
                if grid[x][y] == 2:
                    ans[0] += 1
                return
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x <= m-1 and 0 <= new_y <= n-1:
                    if visited[new_x][new_y] is False and (grid[new_x][new_y] == 0 or grid[new_x][new_y] == 2):
                        visited[new_x][new_y] = True
                        backtrack(new_x, new_y, cnt + 1)
                        visited[new_x][new_y] = False

        m, n  = len(grid), len(grid[0])
        start_x, start_y, total_block = -1, -1, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                if grid[i][j] == -1:
                    total_block += 1
                    
        ans, total = [0], m * n - total_block
        visited = [[False for j in range(n)] for i in range(m)]
        backtrack(start_x, start_y, 1)
        return ans[0]