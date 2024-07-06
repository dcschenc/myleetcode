from collections import deque
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        def dfs(i: int, j: int, c: int) -> None:
            vis[i][j] = True
            for a, b in pairwise((-1, 0, 1, 0, -1)):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n:
                    if not vis[x][y]:
                        if grid[x][y] == c:
                            dfs(x, y, c)
                        else:
                            grid[i][j] = color
                else:
                    grid[i][j] = color

        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]
        dfs(row, col, grid[row][col])
        return grid

        
        m, n = len(grid), len(grid[0])
        queue = deque()
        queue.append((row, col))
        visited = set()
        target = grid[row][col]
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newX, newY = x + dx, y + dy
                    if 0 <= newX <= m-1 and 0 <= newY <= n-1 and grid[newX][newY] == target:
                        queue.append((newX, newY))

        ans = [[grid[i][j] for j in range(n)] for i in range(m)]
        # print(ans, visited)
        
        for x, y in visited:
            if x in (0, m - 1) or y in (0, n-1):
                ans[x][y] = color
                continue
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if grid[x + dx][y + dy] != target:
                    ans[x][y] = color
                    break
        return ans