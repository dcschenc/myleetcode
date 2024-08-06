class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Create a matrix initialized with zeros
        matrix = [[0] * n for _ in range(n)]
      
        # Apply the query operations using a prefix sum approach
        for x1, y1, x2, y2 in queries:
            # Increment the top-left corner of the range by 1
            matrix[x1][y1] += 1          
            # Decrement the positions just outside the range
            if x2 + 1 < n:
                matrix[x2 + 1][y1] -= 1
            if y2 + 1 < n:
                matrix[x1][y2 + 1] -= 1
            if x2 + 1 < n and y2 + 1 < n:
                # This position was decremented twice, so we increment it once
                matrix[x2 + 1][y2 + 1] += 1

        # Convert the operations to actual values by propagating the increments
        for i in range(n):
            for j in range(n):
                # If not in the first row, add value from the cell directly above
                if i > 0:
                    matrix[i][j] += matrix[i - 1][j]
                # If not in the first column, add value from the cell directly to the left
                if j > 0:
                    matrix[i][j] += matrix[i][j - 1]
                # If not in the first row or column, subtract the value from 
                # the cell to the top-left to counteract double counting
                if i > 0 and j > 0:
                    matrix[i][j] -= matrix[i - 1][j - 1]
      
        # The resultant matrix contains the final values after all queries
        return matrix