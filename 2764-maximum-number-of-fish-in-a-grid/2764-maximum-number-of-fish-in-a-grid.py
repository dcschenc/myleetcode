class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2658.Maximum%20Number%20of%20Fish%20in%20a%20Grid
        def dfs(i: int, j: int) -> int:
            cnt = grid[i][j]
            grid[i][j] = 0
            for a, b in pairwise((-1, 0, 1, 0, -1)):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    cnt += dfs(x, y)
            return cnt

        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans = max(ans, dfs(i, j))
        return ans


        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    queue = deque()
                    queue.append((i, j))
                    visited = set()
                    cur = 0
                    while queue:
                        for _ in range(len(queue)):
                            x, y = queue.popleft()
                            if (x, y) in visited:
                                continue
                            visited.add((x, y))                            
                            cur += grid[x][y]
                            grid[x][y] = 0
                            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                                new_x, new_y = x + dx, y + dy
                                if 0 <= new_x <= m-1 and 0 <= new_y <= n-1 and grid[new_x][new_y] > 0:
                                    queue.append((new_x, new_y))
                    ans = max(ans, cur)
        return ans