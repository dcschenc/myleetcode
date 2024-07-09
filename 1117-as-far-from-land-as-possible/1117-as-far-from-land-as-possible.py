from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:        
        n = len(grid)
        if len(set([grid[i][j] for i in range(n) for j in range(n)])) == 1:
            return -1
        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
        visited = set()
        steps = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + dx, j + dy
                    if 0 <= x <= n-1 and 0 <= y <= n-1 and grid[x][y] == 0:
                        grid[x][y] = 1
                        queue.append((x, y))
            steps += 1
        return steps - 1