class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1463.Cherry%20Pickup%20II
        # Get dimensions of the grid
        rows, cols = len(grid), len(grid[0])
      
        # Initialize the DP table f with -1, to store the cherries picked up for each (j1, j2) pair
        f = [[-1] * cols for _ in range(cols)]
      
        # Initialize temporary DP table to store the next row values
        temp_dp = [[-1] * cols for _ in range(cols)]
      
        # Base case initialization: starting at the first row
        f[0][cols - 1] = grid[0][0] + grid[0][cols - 1]
      
        # Start filling the DP table from the second row
        for row in range(1, rows):
            for j1 in range(cols):
                for j2 in range(cols):
                    # Collect cherries for current positions (j1, j2), avoid double collecting if j1 == j2
                    cherries = grid[row][j1] + (0 if j1 == j2 else grid[row][j2])
                  
                    # Transition from previous positions (y1, y2) to current (j1, j2)
                    for y1 in range(max(j1 - 1, 0), min(j1 + 2, cols)):
                        for y2 in range(max(j2 - 1, 0), min(j2 + 2, cols)):
                            if f[y1][y2] != -1:  # Valid previous state
                                temp_dp[j1][j2] = max(temp_dp[j1][j2], f[y1][y2] + cherries)
          
            # Swap the tables: make temp_dp the new DP table and reset temp_dp for the next iteration
            f, temp_dp = temp_dp, [[-1] * cols for _ in range(cols)]

        # Find the maximum cherries that can be collected for all (j1, j2) pairs in the last row
        return max(f[j1][j2] for j1, j2 in product(range(cols), range(cols)))
