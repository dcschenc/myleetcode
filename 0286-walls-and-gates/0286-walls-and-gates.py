from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """        
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        inf = 2 ** 31 - 1
        visited = set()
        while queue:               
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                for dx, dy in dr:
                    x, y = i + dx, j + dy                   
                    if 0 <= x <= m-1 and 0 <= y <= n-1 and rooms[x][y] != -1 :
                        if rooms[x][y] == inf:
                            rooms[x][y] = rooms[i][j] + 1
                        queue.append((x, y))    
                    
        # m, n = len(rooms), len(rooms[0])
        # dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # inf = 2**31 - 1
        # for i in range(m):
        #     for j in range(n):
        #         if rooms[i][j] == inf:
        #             queue = deque()
        #             queue.append((i, j))
        #             visited = set()
        #             level = 1
        #             found = False
        #             while queue:
        #                 for _ in range(len(queue)):
        #                     x, y = queue.popleft()
        #                     if (x, y) in visited:
        #                         continue
        #                     visited.add((x, y))                        
        #                     for dx, dy in dr:
        #                         nx, ny = x + dx, y + dy
        #                         if 0 <= nx <= m-1 and 0 <= ny <= n-1 and rooms[nx][ny] != -1:
        #                             if rooms[nx][ny] == 0:
        #                                 rooms[i][j] = level
        #                                 found = True
        #                                 break
        #                             queue.append((nx, ny))
        #                 if found:
        #                     break
        #                 level += 1
                   