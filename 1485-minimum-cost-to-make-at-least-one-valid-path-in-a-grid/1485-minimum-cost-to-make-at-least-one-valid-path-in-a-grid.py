from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:       
        adj = defaultdict(list)
        dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                for dx, dy in dr:
                    x = i + dx
                    y = j + dy
                    if 0 <= x <= m-1 and 0 <= y <= n-1:
                        if grid[i][j] == 1 and y == j + 1 or grid[i][j] == 2 and y == j-1 or \
                        grid[i][j] == 3 and x == i+1 or grid[i][j] == 4 and x == i-1 :
                            adj[(i,j)].append((x, y, 0))
                        else:
                            adj[(i, j)].append((x, y, 1))           

        ### bfs ###
        minheap = [(0, 0, 0)]
        shortest = {}
        while minheap:
            w, i, j = heappop(minheap)      
            for nbx, nby, w2 in adj[(i, j)]:
                if (nbx, nby) not in shortest or w + w2 < shortest[(nbx, nby)]:
                    shortest[(nbx, nby)] = w + w2
                    heappush(minheap, (w+w2, nbx, nby))
        return shortest[(m-1, n-1)] if (m-1, n-1) in shortest else 0
        
