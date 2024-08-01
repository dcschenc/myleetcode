class Solution:
    def countCollisions(self, directions: str) -> int:
        # https://algo.monster/liteproblems/2211
        # Strip 'L' from the left end and 'R' from the right end of the directions string
        # # because 'L' at the start or 'R' at the end won't cause any collisions.
        # sanitized_directions = directions.lstrip('L').rstrip('R')
        # # Count the number of collisions:
        # # Total number of cars that can collide is the length of the sanitized directions
        # # subtracted by the number of 'S' (stationary) cars since 'S' cars do not move.
        # collisions = len(sanitized_directions) - sanitized_directions.count('S')

        # return collisions

        stack = []
        collisions = 0
        for d in directions:
            if d == 'R':
                stack.append('R')
                continue
            if d == 'L':
                if not stack:
                    continue
                collisions += 2 if stack[-1] == 'R' else 1
                stack.pop()
                d = 'S'
            if d == 'S':
                while stack and stack[-1] == 'R':
                    stack.pop()
                    collisions += 1
                stack.append('S')
        return collisions