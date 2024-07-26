class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            covered = grid1[i][j]
            grid2[i][j] = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and grid2[x][y] and not dfs(x, y):
                    covered = 0
            return covered

        m, n = len(grid1), len(grid1[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        ans += 1
        return ans
        # return sum(dfs(i, j) for i in range(m) for j in range(n) if grid2[i][j])

        m, n = len(grid1), len(grid1[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    covered = True
                    visited = set()
                    queue = deque([(i, j)])
                    while queue:
                        for _ in range(len(queue)):
                            x, y = queue.popleft()
                            if (x, y) in visited:
                                continue
                            visited.add((x, y))
                            if grid1[x][y] == 0:
                                covered = False
                            grid2[x][y] = 0
                            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                                new_x, new_y = x + dx, y + dy
                                if 0 <= new_x <= m-1 and 0 <= new_y <= n-1 and grid2[new_x][new_y] == 1:
                                    queue.append((new_x, new_y))
                    if covered:
                        ans += 1
        return ans