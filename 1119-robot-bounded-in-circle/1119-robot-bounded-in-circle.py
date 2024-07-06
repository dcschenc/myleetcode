class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Initialize the direction index, 0 = North, 1 = West, 2 = South, 3 = East
        direction_index = 0
      
        # Initialize distances for all four directions,
        # index corresponds to the direction: 0 = North, 1 = West, 2 = South, 3 = East
        distances = [0, 0, 0, 0]
      
        # Loop through each character in the instructions string
        for command in instructions:
            if command == 'L':
                # Turn left: Update direction_index counter-clockwise
                direction_index = (direction_index + 1) % 4
            elif command == 'R':
                # Turn right: Update direction_index clockwise
                direction_index = (direction_index + 3) % 4
            else:  # command == 'G'
                # Move forward: Increment distance in the current facing direction
                distances[direction_index] += 1
      
        # Check if the robot returns to the original position (circular) OR
        # is facing in a different direction other than North after one cycle of instructions
        # This ensures that repeating the instructions will eventually bring it back to the origin.
        is_circular = (distances[0] == distances[2] and distances[1] == distances[3]) or direction_index != 0
      
        return is_circular
        

        # north = 0, east = 1, south = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Initial position is in the center
        x = y = 0
        # facing north
        idx = 0
        
        for i in instructions:
            if i == "L":
                idx = (idx + 3) % 4
            elif i == "R":
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]
        
        # after one cycle:
        # robot returns into initial position
        # or robot doesn't face north
        return (x == 0 and y == 0) or idx != 0