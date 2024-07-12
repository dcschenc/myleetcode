class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            res = True if 0 < x < m-1 and 0 < y < n-1 else False     
            grid[x][y] = 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x <= m-1 and 0 <= new_y <= n-1 and grid[new_x][new_y] == 0:
                    res = res & dfs(new_x, new_y)
            return res
        m, n = len(grid), len(grid[0])
        return sum(dfs(x, y) for y in range(n) for x in range(m) if grid[x][y] == 0)


        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue = deque()
                    visited = set()
                    queue.append((i, j))
                    closed = True
                    while queue:
                        for _ in range(len(queue)):
                            x, y = queue.popleft()
                            if (x, y) in visited:
                                continue
                            visited.add((x, y))
                            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                                new_x, new_y = x + dx, y + dy
                                if new_x < 0 or new_x > m - 1 or new_y < 0 or new_y > n - 1:
                                    closed = False
                                    continue
                                if grid[new_x][new_y] == 1:
                                    continue
                                queue.append((new_x, new_y))
                                grid[new_x][new_y] = 1
                    if closed:
                        ans += 1
        return ans