from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            dirs = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for new_x, new_y in dirs:
                if 0 <= new_x <m and 0<= new_y <n:
                    if grid[new_x][new_y] == '1' and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        dfs(new_x, new_y)
        
        visited = set()
        count = 0
        m, n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    dfs(i, j)                    
        return count
    
    
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def bfs(i, j):
#             queue = deque()
#             queue.append((i, j))
#             visited.add((i,j))
#             while len(queue) > 0:
#                 x, y = queue.popleft()
#                 dirs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
#                 for new_x, new_y in dirs:
#                     if 0<=new_x<m and 0<=new_y<n:
#                         if grid[new_x][new_y] == '1' and (new_x, new_y) not in visited:
#                             queue.append((new_x, new_y))                            
#                             visited.add((new_x, new_y))
#         visited = set()
#         count = 0
#         m, n = len(grid),len(grid[0])
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1' and (i, j) not in visited:
#                     count += 1
#                     bfs(i, j)                    
#         return count
    