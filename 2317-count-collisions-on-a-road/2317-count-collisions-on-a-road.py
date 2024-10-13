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
        d = directions.lstrip('L').rstrip('R')
        return len(d) - d.count('S')