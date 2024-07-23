from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    queue.append((i, j))
                    break
        steps = 1
        dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()                
                if (i, j) in seen:
                    continue
                seen.add((i, j))
                for dx, dy in dr:
                    x, y = i + dx, j + dy
                    if 0 <= x <= m-1 and 0 <= y <= n-1 and (x, y) not in seen:
                        if grid[x][y] == 'O':
                            queue.append((x, y))
                        elif grid[x][y] == '#':                           
                                return steps
            steps += 1
        return -1