# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1778.Shortest%20Path%20in%20a%20Hidden%20Grid
        # Use depth-first search to explore the grid
        def dfs(x, y):
            nonlocal target  # To modify the target variable outside of the nested function
            if master.isTarget():  # Check if current position is the target
                target = (x, y)
            for direction, opposite_direction, dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if master.canMove(direction) and (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))  # Mark the cell as visited
                    master.move(direction)  # Move to the next cell
                    dfs(next_x, next_y)  # Perform DFS from the next cell
                    master.move(opposite_direction)  # Move back

        # Define possible movement directions and their opposites
        DIRECTIONS = [
            ('U', 'D', -1, 0),
            ('D', 'U', 1, 0),
            ('L', 'R', 0, -1),
            ('R', 'L', 0, 1),
        ]

        target = None  # To keep track of the target's position
        visited = set()  # To keep track of visited cells
        dfs(0, 0)  # Start DFS from the origin (0, 0), 就是一开始robot在的位置

        if target is None:  # If target was not found during DFS
            return -1  # Return -1 indicating no path exists to the target

        # Use breadth-first search to find the shortest path to target
        visited.remove((0, 0))  # Remove the starting cell from visited set
        queue = deque([(0, 0)])  # Initialize queue with starting cell
        steps = 0  # Counter for the number of steps taken

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) == target:  # If current cell is the target
                    return steps  # Return the number of steps taken
          
                for _, _, dx, dy in DIRECTIONS:
                    next_x, next_y = x + dx, y + dy
                    if (next_x, next_y) in visited:
                        visited.remove((next_x, next_y))  # Mark cell as visited
                        queue.append((next_x, next_y))  # Enqueue the next cell
          
            steps += 1  # Increment step count after exploring all cells at current level
      
        return -1  # If target cannot be reached, return -1