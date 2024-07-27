from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:        
        m, n = len(maze), len(maze[0])
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        visited = set()
        visited.add(tuple(entrance))
        while queue:
            x, y, steps = queue.popleft()
            moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for i, j in moves:
                if 0<=i<m and 0<=j<n and maze[i][j] == '.' and (i, j) not in visited:
                    if i in [0, m-1] or j in [0, n-1]:
                        return steps+1
                    queue.append((i,j, steps+1))
                    visited.add((i,j))
        return -1
