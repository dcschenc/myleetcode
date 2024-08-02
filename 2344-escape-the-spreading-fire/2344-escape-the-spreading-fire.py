class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        # https://algo.monster/liteproblems/2258
        # Helper function to spread fire by one step
        def spread_fire(fire_queue: deque) -> deque:
            new_fire_queue = deque()
            while fire_queue:
                row, col = fire_queue.popleft()
                for delta_row, delta_col in pairwise(fire_directions):
                    x, y = row + delta_row, col + delta_col
                    if 0 <= x < rows and 0 <= y < cols and not is_on_fire[x][y] and grid[x][y] == 0:
                        is_on_fire[x][y] = True
                        new_fire_queue.append((x, y))
            return new_fire_queue

        # Helper function to check if it's possible to escape with a given head start
        def can_escape_with_head_start(head_start: int) -> bool:
            # Reset the fire spread simulation
            for i in range(rows):
                for j in range(cols):
                    is_on_fire[i][j] = False
          
            fire_queue = deque()
            for i, row in enumerate(grid):
                for j, cell in enumerate(row):
                    if cell == 1:
                        is_on_fire[i][j] = True
                        fire_queue.append((i, j))

            # Let the fire spread for 'head_start' steps
            while head_start and fire_queue:
                fire_queue = spread_fire(fire_queue)
                head_start -= 1
          
            # If the starting cell is on fire, not possible to escape
            if is_on_fire[0][0]:
                return False

            # Queue for BFS to check for an escape path
            escape_queue = deque([(0, 0)])
            visited = [[False] * cols for _ in range(rows)]
            visited[0][0] = True
          
            while escape_queue:
                for _ in range(len(escape_queue)):
                    row, col = escape_queue.popleft()
                    if is_on_fire[row][col]:
                        continue
                    for delta_row, delta_col in pairwise(fire_directions):
                        x, y = row + delta_row, col + delta_col
                        if (0 <= x < rows and 0 <= y < cols and not visited[x][y] and not is_on_fire[x][y] and grid[x][y] == 0):
                            if x == rows - 1 and y == cols - 1:
                                return True
                            visited[x][y] = True
                            escape_queue.append((x, y))
                # Spread fire after each step of player movement
                fire_queue = spread_fire(fire_queue)
            return False

        # Initialize parameters
        rows, cols = len(grid), len(grid[0])
        fire_directions = (-1, 0, 1, 0, -1)  # Directions for fire to spread
        is_on_fire = [[False] * cols for _ in range(rows)]
      
        # Binary search for the maximum minutes
        left, right = -1, rows * cols
        while left < right:
            mid = (left + right + 1) // 2
            if can_escape_with_head_start(mid):
                left = mid
            else:
                right = mid - 1
      
        # Return the maximum minutes if the player can escape, else return large number
        return int(1e9) if left == rows * cols else left
