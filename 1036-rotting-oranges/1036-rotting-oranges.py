from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minutes = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        while queue:
            flag = False          
            for i in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        queue.append((new_x, new_y))
                        flag = True
            if flag:
                minutes += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minutes