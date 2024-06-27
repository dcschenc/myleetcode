from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            if grid[i][j] == 0:
                return 0
            ans = 1
            grid[i][j] = 0
            dirs = (-1, 0, 1, 0, -1)
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n:
                    ans += dfs(x, y)
            return ans

        m, n = len(grid), len(grid[0])
        return max(dfs(i, j) for i in range(m) for j in range(n))
        
        def bfs(i, j):            
            nonlocal ans
            queue = deque()
            queue.append((i, j))
            visited = set()
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    grid[x][y] = 0
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x <= m-1 and 0 <= new_y <= n-1 and grid[new_x][new_y] == 1:
                            queue.append((new_x, new_y))
            ans = max(ans, len(visited))       

        m, n = len(grid), len(grid[0])
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
        return ans