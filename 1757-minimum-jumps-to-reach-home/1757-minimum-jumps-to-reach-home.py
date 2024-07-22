class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1654.Minimum%20Jumps%20to%20Reach%20Home
        forbidden = set(forbidden)
        queue = deque()
        queue.append((0, 0))
        steps = 0
        visited = set()
        while queue:
            for _ in range(len(queue)):
                pos, direction = queue.popleft()
                if pos == x:
                    return steps
                if (pos, direction) in visited:
                    continue
                visited.add((pos, direction))
                if pos + a not in forbidden and 0 <= pos + a <= 6000:
                    queue.append((pos + a, 1))
                if direction != 2 and pos - b not in forbidden and 0 <= pos - b <= 6000:
                    queue.append((pos - b, 2))
            steps += 1
        return -1

        # Initialize a set of forbidden positions
        forbidden_set = set(forbidden)
      
        # Queue for breadth-first search with position and whether the last movement was forward (1) or backward (0)
        queue = deque([(0, 1)])
      
        # Visited set to keep track of positions and their last movement direction
        visited = {(0, 1)}
      
        # Step counter starting from 0
        steps = 0
      
        # Start breadth-first search
        while queue:
            # Process nodes level by level
            for _ in range(len(queue)):
                position, last_movement_forward = queue.popleft()
              
                # If the current position is the target, return the number of steps
                if position == x:
                    return steps
              
                # List of possible next positions
                next_positions = [(position + a, 1)]  # always can go forward
              
                # Can only go backward if the last movement was forward
                if last_movement_forward:
                    next_positions.append((position - b, 0))
              
                # Iterate over possible next positions
                for next_position, next_movement_forward in next_positions:
                    # Check if within bounds, not forbidden, and not already visited
                    if (0 <= next_position < 6000 and 
                        next_position not in forbidden_set and 
                        (next_position, next_movement_forward) not in visited):
                      
                        # Add to queue and mark as visited
                        queue.append((next_position, next_movement_forward))
                        visited.add((next_position, next_movement_forward))
          
            # Increment steps after finishing processing the current level
            steps += 1
      
        # Return -1 if it's not possible to reach the target
        return -1