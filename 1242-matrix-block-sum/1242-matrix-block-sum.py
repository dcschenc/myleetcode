class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1314.Matrix%20Block%20Sum
       
        # Helper function to get the cumulative sum up to (i, j) in the prefix sum matrix
        def get_cumulative_sum(i, j):
            # Boundary check to ensure indices fall within the valid range
            i = max(min(num_rows, i), 0)
            j = max(min(num_cols, j), 0)
            return prefix_sum[i][j]

        # Get the dimensions of the matrix
        num_rows, num_cols = len(mat), len(mat[0])
      
        # Initialize a prefix sum matrix with one extra row and column
        prefix_sum = [[0] * (num_cols + 1) for _ in range(num_rows + 1)]
      
        # Populate the prefix sum matrix
        for row in range(1, num_rows + 1):
            for col in range(1, num_cols + 1):
                prefix_sum[row][col] = (
                    prefix_sum[row - 1][col] +
                    prefix_sum[row][col - 1] -
                    prefix_sum[row - 1][col - 1] +
                    mat[row - 1][col - 1]
                )

        # Initialize the answer matrix with zeros
        answer = [[0] * num_cols for _ in range(num_rows)]
      
        # Compute the block sum for each element in the matrix
        for row in range(num_rows):
            for col in range(num_cols):
                answer[row][col] = (
                    get_cumulative_sum(row + k + 1, col + k + 1) -
                    get_cumulative_sum(row + k + 1, col - k) -
                    get_cumulative_sum(row - k, col + k + 1) +
                    get_cumulative_sum(row - k, col - k)
                )
              
        # Return the answer matrix
        return answer