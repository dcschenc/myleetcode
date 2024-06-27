class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # https://algo.monster/liteproblems/741

        n = len(grid)      
        # Initialize the dynamic programming table with negative infinity
        dp = [[[-float('inf')] * n for _ in range(n)] for _ in range(2 * n - 1)]
        dp[0][0][0] = grid[0][0]  # Starting point
      
        # Iterate over all possible steps `k` from top-left to bottom-right
        for k in range(1, 2 * n - 1):  # 1, 2*n - 2
            for i1 in range(n):
                for i2 in range(n):
                    # Calculate positions for both paths on step k
                    j1, j2 = k - i1, k - i2
                  
                    # Continue if out of bounds or hits a thorn
                    if (
                        not 0 <= j1 < n 
                        or not 0 <= j2 < n 
                        or grid[i1][j1] == -1 
                        or grid[i2][j2] == -1
                    ):
                        continue
                  
                    # Collect cherries from the current cell(s)
                    cherries = grid[i1][j1]
                    if i1 != i2:
                        cherries += grid[i2][j2]
                  
                    # Check all previous step combinations to get the maximum cherries
                    dp[k][i1][i2] = max(dp[k][i1][i2], dp[k - 1][i1-1][i2] + cherries)
                    dp[k][i1][i2] = max(dp[k][i1][i2], dp[k - 1][i1][i2 -1] + cherries)
                    dp[k][i1][i2] = max(dp[k][i1][i2], dp[k - 1][i1 -1][i2 - 1] + cherries)
                    dp[k][i1][i2] = max(dp[k][i1][i2], dp[k - 1][i1][i2] + cherries)
                            
                    # for prev_i1 in range(i1 - 1, i1 + 1):
                    #     for prev_i2 in range(i2 - 1, i2 + 1):
                    #         if prev_i1 >= 0 and prev_i2 >= 0:
                    #             dp[k][i1][i2] = max(
                    #                 dp[k][i1][i2], dp[k - 1][prev_i1][prev_i2] + cherries
                    #             )
      
        # Return the maximum cherries collectible, ensuring non-negative result
        return max(0, dp[-1][-1][-1])



        def dfs(row1, col1, row2):
            col2 = row1 + col1 - row2
            if row1 == n or col1 == n or row2 == n or col2 == n or grid[row1][col1] == -1 or grid[row2][col2] == -1:
                return float('-inf')
            
            if row1 == col1 == row2 == col2 == n - 1:
                return grid[row1][col1]
            
            if dp[row1][col1][row2] != -1:
                return dp[row1][col1][row2]
            
            cherries = grid[row1][col1]
            
            if row1 != row2 or col1 != col2:
                cherries += grid[row2][col2]
            
            cherries += max(dfs(row1 + 1, col1, row2 + 1), dfs(row1, col1 + 1, row2),
                            dfs(row1 + 1, col1, row2), dfs(row1, col1 + 1, row2 + 1))
            
            dp[row1][col1][row2] = cherries
            return cherries


        n = len(grid)
        dp = [[[-1] * n for _ in range(n)] for _ in range(n)]      

        result = max(0, dfs(0, 0, 0))
        return result