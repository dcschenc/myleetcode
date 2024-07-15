from collections import deque
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:       
        rows, cols = len(grid), len(grid[0])
        
        # Directions: left, right, up, down
        directions = {
            1: [(0, -1), (0, 1)],   # left ↔ right
            2: [(-1, 0), (1, 0)],   # top ↕ bottom
            3: [(0, -1), (1, 0)],   # left ↔ bottom
            4: [(0, 1), (1, 0)],    # right ↔ bottom
            5: [(0, -1), (-1, 0)],  # left ↔ top
            6: [(0, 1), (-1, 0)]    # right ↔ top
        }
        
        # Compatibility for the next cell to move into  (opposite direction)
        compatibility = {
            (0, -1): [1, 4, 6],     # moving left: type 1, 4, 6
            (0, 1): [1, 3, 5],      # moving right: type 1, 3, 5
            (-1, 0): [2, 3, 4],     # moving up: type 2, 3, 4
            (1, 0): [2, 5, 6]       # moving down: type 2, 5, 6
        }
        
        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols
        
        queue = deque([(0, 0)])
        visited = set((0, 0))
        
        while queue:
            x, y = queue.popleft()
            
            if x == rows - 1 and y == cols - 1:
                return True
            
            for dx, dy in directions[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and (nx, ny) not in visited and grid[nx][ny] in compatibility[(dx, dy)]:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        
        return False

        # def get_next(i, j):
        #     next_cells = []
        #     cur = grid[i][j]
        #     left, right = [1, 3, 5], [1, 4, 6]
        #     up, down = [2, 5, 6], [2, 3, 4]
        #     if cur in left and j - 1 >= 0 and grid[i][j-1] in right:
        #         next_cells.append((i, j - 1))
        #     if cur in right and j + 1 <= n - 1 and grid[i][j + 1] in left:
        #         next_cells.append((i, j + 1))
        #     if cur in down and i + 1 <= m - 1 and grid[i + 1][j] in up:
        #         next_cells.append((i + 1, j))
        #     if cur in up and i - 1 >= 0 and grid[i - 1][j] in down:
        #         next_cells.append((i - 1, j))
        #     return next_cells

        # m, n = len(grid), len(grid[0])
        # queue = deque()
        # queue.append((0, 0))
        # visited = set()
        # while queue:
        #     for _ in range(len(queue)):
        #         i, j = queue.popleft()
        #         if i == m-1 and j == n-1:
        #             return True
        #         if (i, j) in visited:
        #             continue
        #         visited.add((i, j))
        #         next_cells = get_next(i, j)
        #         for x, y in next_cells:
        #             queue.append((x, y))
        # return False

