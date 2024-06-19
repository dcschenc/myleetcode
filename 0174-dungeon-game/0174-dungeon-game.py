class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # https://algo.monster/liteproblems/174
        # Get the dimensions of the dungeon matrix.
        num_rows, num_columns = len(dungeon), len(dungeon[0])
      
        # Initialize dp (Dynamic Programming) matrix with infinity.
        # An extra row and column are added to handle the edge cases easily.
        dp = [[inf] * (num_columns + 1) for _ in range(num_rows + 1)]
      
        # The hero needs at least 1 HP to reach the princess.
        # Initialize the cell to the princess's right and the one below her to 1.
        dp[num_rows][num_columns - 1] = dp[num_rows - 1][num_columns] = 1
      
        # Start from the bottom right corner and move to the top left corner.
        for i in range(num_rows - 1, -1, -1):     # Iterate over rows in reverse
            for j in range(num_columns - 1, -1, -1):  # Iterate over columns in reverse              
                # Find the minimum HP needed to go to the next cell.
                # Cannot have less than 1 HP, hence the max with 1.
                min_hp_on_exit = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(1, min_hp_on_exit)
      
        # Return the HP needed at the start (0,0) to guarantee reaching the princess.
        return dp[0][0]