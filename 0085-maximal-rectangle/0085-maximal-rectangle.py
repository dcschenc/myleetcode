class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # https://algo.monster/liteproblems/85
        
        # This function finds the maximal rectangle of '1's in a binary matrix.
      
        # Initialize the heights array with zeros based on the width of the matrix
        heights = [0] * len(matrix[0])
        # Initialize the answer to 0, which will hold the area of the largest rectangle
        max_area = 0
      
        # Iterate through each row in the binary matrix
        for row in matrix:
            # Update heights reflecting continuous '1's in a column
            for col_idx, val in enumerate(row):  # col_idx is the index, val is the value at that position
                if val == "1":
                    # Increase the current column's height if the row value is a '1'
                    heights[col_idx] += 1
                else:
                    # Reset the height to 0 if the row value is '0'
                    heights[col_idx] = 0
          
            # Update the max_area with the largest rectangle found in the current histogram of heights
            max_area = max(max_area, self.largestRectangleArea(heights))
      
        # Return the maximal rectangle area found
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        # This function calculates the largest rectangle in a histogram.
      
        # Length of the heights list
        num_heights = len(heights)
      
        # Stack to keep track of indices for heights
        stack = []
      
        # Arrays to store indices of left and right smaller heights
        prev_smaller = [-1] * num_heights
        next_smaller = [num_heights] * num_heights
      
        # Forward pass to find previous smaller heights
        for i, height in enumerate(heights):
            # If the current height is lesser than the height at the stack's top index,
            # pop the stack until a smaller height is found
            while stack and heights[stack[-1]] >= height:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)
      
        # Reset stack for next pass
        stack = []
      
        # Backward pass to find next smaller heights
        for i in range(num_heights - 1, -1, -1):
            cur_height = heights[i]
            while stack and heights[stack[-1]] >= cur_height:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)
      
        # Calculate the largest rectangle area by finding the maximum area
        # for each height, considering the distance to the previous and next smaller heights.
        max_area = max(
            height * (next_smaller[i] - prev_smaller[i] - 1) for i, height in enumerate(heights)
        )
      
        # Return the maximum area found
        return max_area
