class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2852.Sum%20of%20Remoteness%20of%20All%20Cells
        def dfs(i: int, j: int) -> (int, int):
            s, t = grid[i][j], 1
            grid[i][j] = 0
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if 0 <= x < n and 0 <= y < n and grid[x][y] > 0:
                    s1, t1 = dfs(x, y)
                    s, t = s + s1, t + t1
            return s, t

        n = len(grid)
        dirs = (-1, 0, 1, 0, -1)
        cnt = sum(x > 0 for row in grid for x in row)
        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x > 0:
                    s, t = dfs(i, j)
                    ans += (cnt - t) * s
        return ans


        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            subtotal = 0
            visited = set()
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    if (x, y) in visited:
                        continue
                    subtotal += grid[x][y]
                    visited.add((x, y))
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx <= m-1 and 0 <= ny <= n-1 and grid[nx][ny] != -1:
                            queue.append((nx, ny))
            return subtotal, visited
        
        ans, total = 0, 0
        m, n = len(grid), len(grid[0])
        visited_total = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:                   
                    total += grid[i][j]
        connected = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1 and (i, j) not in connected:
                    subtotal, visited = bfs(i, j)
                    ans = ans + (total - subtotal) * len(visited)
                    connected.update(visited)
        return ans