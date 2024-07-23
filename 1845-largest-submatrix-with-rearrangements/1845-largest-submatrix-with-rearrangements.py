class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # https://leetcode.com/problems/largest-submatrix-with-rearrangements/
        # Get the dimensions of the matrix
        rows, cols = len(matrix), len(matrix[0])
        
        # Initialize the height matrix
        height = [[0] * cols for _ in range(rows)]
        
        # Fill the height matrix
        for j in range(cols):
            for i in range(rows):
                if matrix[i][j] == 1:
                    height[i][j] = height[i-1][j] + 1 if i > 0 else 1
        
        # Initialize the maximum area
        max_area = 0
        
        # For each row, sort the heights in descending order
        for i in range(rows):
            sorted_heights = sorted(height[i], reverse=True)
            
            # Calculate the maximum area for the current row
            for j in range(cols):
                max_area = max(max_area, sorted_heights[j] * (j + 1))
        
        return max_area

        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        for row in range(m):
            for col in range(n):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]

            curr_row = sorted(matrix[row], reverse=True)
            for i in range(n):
                ans = max(ans, curr_row[i] * (i + 1))

        return ans