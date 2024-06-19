class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Get the dimensions of the matrix
        m, n = len(matrix), len(matrix[0])        
        # Initialize the dp array
        dp = [[0] * n for _ in range(m)]        
        # Initialize the max size of the square seen so far
        max_size = 0
        
        # Fill the dp array
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        # First row or column, so the maximum size of the square is 1
                        dp[i][j] = 1
                    else:
                        # Check the values of the cells to the left, top, and top-left of the current cell
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    # Update the max size of the square seen so far
                    max_size = max(max_size, dp[i][j])
        
        # Return the area of the largest square
        return max_size * max_size
        
        # m, n = len(matrix), len(matrix[0])
        # dp = [[0 for i in range(n)] for j in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0:                    
        #             if matrix[i][j] == '1':
        #                 dp[i][j] = 1                   
        #         elif j == 0:                    
        #             if matrix[i][j] == '1':
        #                 dp[i][j] = 1                        
        #         else:
        #             if matrix[i][j] == '1':
        #                 # if matrix[i-1][j] == '1' and matrix[i][j-1] == '1'and matrix[i-1][j-1] == '1':                          
        #                 if dp[i-1][j] == dp[i][j-1]:
        #                     # tmp = dp[i-1][j]
        #                     if dp[i-1][j-1] >= dp[i-1][j]:
        #                         dp[i][j] = dp[i-1][j]+ 1
        #                     else:
        #                         dp[i][j] = dp[i-1][j]
        #                 else:
        #                     dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        #                 # else:
        #                 #     dp[i][j] = 1
        # max_l = 0
        # # print(dp)
        # for i in range(m):
        #     for j in range(n):
        #         if dp[i][j] > max_l:
        #             max_l = dp[i][j]
        # return max_l*max_l
