class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Create a queue for breadth-first search and initialize it with an empty state.
        queue = deque([0])
        # Initialize the number of steps (minimum stickers) to 0.
        steps = 0
        # Calculate the length of the target word.
        n = len(target)
        # Create a visited states list to prevent repeated processing of the same state.
        visited = [False] * (1 << n)
        # Mark the empty state as visited.
        visited[0] = True  
      
        # Start the breadth-first search.
        while queue:
            # Process all the states at the current level.
            for _ in range(len(queue)):
                current_state = queue.popleft()
              
                # If all characters are used, return the number of steps.
                if current_state == (1 << n) - 1:
                    return steps
              
                # Try all stickers for the current state.
                for sticker in stickers:
                    next_state = current_state
                    sticker_count = Counter(sticker)
                  
                    # Attempt to match sticker characters with target characters.
                    for i, char in enumerate(target):
                        # If the character at position i is not yet added, and the sticker has the char.
                        if not (next_state & (1 << i)) and sticker_count[char]:
                            next_state |= 1 << i
                            sticker_count[char] -= 1                          
                    # If the next state has not been visited, mark it as visited and add to the queue.
                    if not visited[next_state]:
                        visited[next_state] = True
                        queue.append(next_state)
          
            # Increment the step count after processing all states at the current level.
            steps += 1
      
        # If target cannot be reached return -1 indicating not possible.
        return -1
