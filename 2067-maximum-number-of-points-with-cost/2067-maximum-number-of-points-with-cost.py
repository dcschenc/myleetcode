class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1937.Maximum%20Number%20of%20Points%20with%20Cost
        m, n = len(points), len(points[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[0][j] = points[0][j]
        for i in range(1, m):
            left_max = float('-inf')
            for j in range(n):
                left_max = max(left_max, dp[i-1][j] + j )
                dp[i][j] = max(dp[i][j], points[i][j] + left_max - j)
            right_max = float('-inf')
            for j in range(n-1, -1, -1):
                right_max = max(right_max, dp[i-1][j] - j)
                dp[i][j] = max(dp[i][j], points[i][j] + right_max + j)           

        return max(dp[m-1])


        # Get the number of columns in the points matrix.
        n = len(points[0])
      
        # Initialize dp array with the first row of points.
        dp = points[0][:]
      
        # Iterate over each row in points starting from the second row.
        for row in points[1:]:
            # Create a new row for dp, to store the maximum points for the current row.
            new_dp = [0] * n
          
            # Initialize left max value, this tracks the maximum from the left side including the current position.
            left_max = float('-inf')
            # Left pass: Fill in the new_dp array considering the left side of each column.
            for j in range(n):
                left_max = max(left_max, dp[j] + j)
                new_dp[j] = max(new_dp[j], row[j] + left_max - j)
          
            # Initialize right max value, this tracks the maximum from the right side including the current position.
            right_max = float('-inf')
            # Right pass: Update the new_dp array considering the right side of each column.
            for j in range(n - 1, -1, -1):
                right_max = max(right_max, dp[j] - j)
                new_dp[j] = max(new_dp[j], row[j] + right_max + j)
          
            # Update dp array with the new_dp for the next iteration.
            dp = new_dp
      
        # Return the maximum points that can be collected, which is the max value in the last dp row.
        return max(dp)
        
        m, n = len(points), len(points[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[0][j] = points[0][j]
        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + points[i][j] - abs(j-k))
        return max(dp[m-1])