class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        # https://algo.monster/liteproblems/2174
        
        # Get the dimensions of the grid
        rows, columns = len(grid), len(grid[0])
      
        # Calculate the initial state by converting the grid to a bitmask
        initial_state = sum(1 << (row * columns + col) for row in range(rows) for col in range(columns) if grid[row][col])
      
        # Initialize the queue with the initial state and a set for visited states
        queue = deque([initial_state])
        visited = {initial_state}
      
        # Counter for the number of steps
        steps = 0
      
        # Perform a breadth-first search
        while queue:
            # Iterate through all states at the current level
            for _ in range(len(queue)):
                state = queue.popleft()
              
                # If the state is 0, all ones have been removed
                if state == 0:
                    return steps
              
                # Try turning off each 1 in the grid
                for row in range(rows):
                    for col in range(columns):
                        if grid[row][col] == 1:
                            next_state = state
                          
                            # Turn off all bits in the same column
                            for r in range(rows):
                                next_state &= ~(1 << (r * columns + col))

                            # Turn off all bits in the same row
                            for c in range(columns):
                                next_state &= ~(1 << (row * columns + c))
                          
                            # If the next state hasn't been visited, add it to the queue and visited set
                            if next_state not in visited:
                                visited.add(next_state)
                                queue.append(next_state)
          
            # Increment the number of steps after checking all states at the current level
            steps += 1
      
        # If no solution is found, return -1
        return -1