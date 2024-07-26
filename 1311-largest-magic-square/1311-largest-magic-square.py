class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        # Define a function to check if a square is magic
        def is_magic_square(x1, y1, x2, y2):
            target_sum = row_prefix[x1 + 1][y2 + 1] - row_prefix[x1 + 1][y1]
          
            # Check rows
            for i in range(x1 + 1, x2 + 1):
                if row_prefix[i + 1][y2 + 1] - row_prefix[i + 1][y1] != target_sum:
                    return False
          
            # Check columns
            for j in range(y1, y2 + 1):
                if col_prefix[x2 + 1][j + 1] - col_prefix[x1][j + 1] != target_sum:
                    return False
          
            # Check diagonal from top-left to bottom-right
            diag_sum = sum(grid[x1 + d][y1 + d] for d in range(x2 - x1 + 1))
            if diag_sum != target_sum:
                return False
          
            # Check diagonal from top-right to bottom-left
            diag_sum = sum(grid[x1 + d][y2 - d] for d in range(x2 - x1 + 1))
            if diag_sum != target_sum:
                return False
          
            return True

        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
      
        # Initialize prefix sum matrices for rows and columns
        row_prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        col_prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
      
        # Calculate prefix sums for rows and columns
        for i in range(rows):
            for j in range(cols):
                row_prefix[i + 1][j + 1] = row_prefix[i + 1][j] + grid[i][j]
                col_prefix[i + 1][j + 1] = col_prefix[i][j + 1] + grid[i][j]      

      
        # Loop from largest possible square size down to 2
        # as the smallest magic square is of size 1 by definition
        for size in range(min(rows, cols), 1, -1):
            for i in range(rows - size + 1):
                for j in range(cols - size + 1):
                    if is_magic_square(i, j, i + size - 1, j + size - 1):
                        return size
      
        # If no magic square larger than 1 is found, return 1
        return 1