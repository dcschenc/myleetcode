from collections import deque
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []
        queue = deque()
        queue.append((start[0], start[1]))
        visited = set()        
        levels = 1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if (i, j) in visited: continue    
                if grid[i][j] > 1 and pricing[0] <= grid[i][j] <= pricing[1]:
                    ans.append((levels, grid[i][j], i, j))
                    grid[i][j] = 1
                
                visited.add((i, j))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + dx, j + dy
                    if 0 <= x <= m-1 and 0 <= y <= n-1:
                        if grid[x][y] != 0:
                            queue.append((x,y))
            levels += 1
        ans.sort()
        return [[x[2], x[3]] for x in ans[:k]]

        