# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> int:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        """
        we can easily solve this problem using heap and visited set
        """
        # heap = []
        # visited = {(0, 0)}
        # direction = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
        # heapq.heappush(heap, (0, 0, 0, copy.copy(master)))
        # while len(heap):
        #     cost, i, j, master = heapq.heappop(heap)
        #     if master.isTarget():
        #         return cost
        #     for key, value in direction.items():
        #         if master.canMove(key) and (i + value[0], j + value[1]) not in visited:
        #             master_copy = copy.copy(master)
        #             x = master_copy.move(key)
        #             heapq.heappush(heap, (x + cost, i + value[0], j + value[1], master_copy))
        #             visited.add((i + value[0], j + value[1]))
        # return -1
        
        def dfs(x, y):
            nonlocal target
            if master.isTarget():
                target = (x, y)
            for direction, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if (nx, ny) not in grid and master.canMove(direction):
                    cost = master.move(direction)
                    if cost != -1:  # Valid move
                        grid[(nx, ny)] = cost
                        dfs(nx, ny)
                        master.move(reverse[direction])  # Backtrack

        directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        reverse = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        
        # Use a dictionary to store the grid, with costs
        grid = {}
        target = None
        # Start DFS from the initial position
        start = (0, 0)
        grid[start] = 0
        dfs(0, 0)
        
        if not target:
            return -1
        
        # Use Dijkstra's algorithm to find the minimum cost path
        pq = [(0, 0, 0)]  # (cost, x, y)
        min_cost = {start: 0}
        
        while pq:
            current_cost, x, y = heapq.heappop(pq)
            if (x, y) == target:
                return current_cost
            for dx, dy in directions.values():
                nx, ny = x + dx, y + dy
                if (nx, ny) in grid:
                    new_cost = current_cost + grid[(nx, ny)]
                    if (nx, ny) not in min_cost or new_cost < min_cost[(nx, ny)]:
                        min_cost[(nx, ny)] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))
        
        return -1
