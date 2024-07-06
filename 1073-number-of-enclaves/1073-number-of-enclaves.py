from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    q.append((i, j))
                    grid[i][j] = 0
        dirs = (-1, 0, 1, 0, -1)
        while q:
            i, j = q.popleft()
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if x >= 0 and x < m and y >= 0 and y < n and grid[x][y]:
                    q.append((x, y))
                    grid[x][y] = 0
        return sum(v for row in grid for v in row)
        
        # def bfs(x, y):
        #     queue = deque([(x,y)])
        #     dr = [[1, 0],[-1, 0], [0, 1], [0, -1]]
        #     visited = set()            
        #     while queue:
        #         for i in range(len(queue)):
        #             x, y = queue.popleft()
        #             if (x, y) in visited:
        #                 continue
        #             visited.add((x, y))
        #             grid[x][y] = 0
        #             for i, j in dr:
        #                 new_x, new_y = x + i, y + j
        #                 if 0 <= new_x <= m-1 and 0 <= new_y <= n-1 and grid[new_x][new_y] == 1:
        #                     queue.append((new_x, new_y))

        
        # m, n = len(grid), len(grid[0])
        # for j in range(n):
        #     if grid[0][j] == 1:
        #         bfs(0, j)
        #     if grid[m-1][j] == 1:
        #         bfs(m-1, j)
        # for i in range(m):
        #     if grid[i][0] == 1:
        #         bfs(i, 0)
        #     if grid[i][n-1] == 1:
        #         bfs(i, n-1)
        # result = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             result += 1
        # return result
