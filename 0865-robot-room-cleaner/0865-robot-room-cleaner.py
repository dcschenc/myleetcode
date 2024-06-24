# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    # https://leetcode.com/problems/robot-room-cleaner/editorial/https://leetcode.com/problems/robot-room-cleaner/editorial/
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def go_back():
            """
            Makes the robot go back to the previous cell and restore the original direction.
            """
            robot.turnLeft()
            robot.turnLeft()  # Rotate 180 degrees to face the opposite direction
            robot.move()
            robot.turnLeft()
            robot.turnLeft()  # Rotate another 180 degrees to restore initial direction

        def backtrack(x, y, direction):
            """
            Cleans the room recursively using depth-first search.

            :param x: Current x-coordinate of the robot
            :param y: Current y-coordinate of the robot
            :param direction: Current direction the robot is facing
            """
            visited.add((x, y))
            robot.clean()
          
            # Loop through all directions: 0 - up, 1 - right, 2 - down, 3 - left
            for k in range(4):
                new_direction = (direction + k) % 4
                new_x = x + directions[new_direction]
                new_y = y + directions[new_direction + 1]
              
                if (new_x, new_y) not in visited and robot.move():
                    backtrack(new_x, new_y, new_direction)
                    go_back()  # Go back to the previous cell after cleaning
              
                # Turn the robot clockwise to explore next direction
                robot.turnRight()
      
        # Define directions corresponding to up, right, down, left movements
        # in order: up(-1, 0), right(0, 1), down(1, 0), left(0, -1)
        directions = (-1, 0, 1, 0, -1)      
        # Use a set to keep track of visited cells (coordinates)
        visited = set()      
        # Start the DFS from the starting point (0,0) facing up (direction 0)
        backtrack(0, 0, 0)
