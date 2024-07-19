class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:    
        visited = set()
        m, n = len(grid), len(grid[0])        
        for i in range(m):
            for j in range(n):
                if (i, j) in visited: continue
                queue = deque([[(i, j), None]])                    
                while queue:
                    for _ in range(len(queue)):
                        cur, parent = queue.popleft()
                        x, y = cur
                        if cur in visited:                                
                            return True
                        visited.add(cur)
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            new_x, new_y = x + dx, y + dy
                            if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) != parent and grid[new_x][new_y] == grid[x][y]:                                    
                                queue.append([(new_x, new_y), (x, y)])
        return False

        def dfs(cur, parent):
            x, y = cur
            if cur in visited:
                return True
            visited.add(cur)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) != parent and grid[new_x][new_y] == grid[x][y]:
                    if dfs((new_x, new_y), (x, y)):
                        return True
            return False

        visited = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    if dfs((i, j), (-1, -1)):
                        return True
        return False
 

        def dfs(path):           
            x, y = path[-1]
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x <= m-1 and 0 <= new_y <= n-1 and grid[new_x][new_y] == val:    
                    if len(path) > 1 and path[-2] == (new_x, new_y):
                        continue                  
                    if (new_x, new_y) == root:
                        return True
                    if (new_x, new_y) in path:
                        continue
                                      
                    if dfs(path + [(new_x, new_y)]):
                        return True
            return False

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                root = (i, j)
                
                if dfs([(i, j)]):
                    return True
        return False
        