class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # Define a function to check if a square with side k fits the threshold
        def check_square_fits(k: int) -> bool:
            for i in range(rows - k + 1):
                for j in range(cols - k + 1):
                    # Compute the sum of the square using prefix sum technique
                    square_sum = prefix_sum[i + k][j + k] - prefix_sum[i][j + k] - prefix_sum[i + k][j] + prefix_sum[i][j]
                    # If the sum is within the threshold, then square of side k fits
                    if square_sum <= threshold:
                        return True
            return False

        # Matrix dimensions
        rows, cols = len(mat), len(mat[0])
      
        # Calculate the prefix sum matrix for efficient area sum calculation
        # Padding with an extra row and column filled with 0 for easy calculation
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + mat[i - 1][j - 1]

        # Initialize binary search bounds
        left, right = 0, min(rows, cols)
      
        # Perform binary search to find the maximum square side length
        while left < right:
            mid = (left + right + 1) // 2 # Use integer division for Python 3
            # Check if there's a square with the current mid side length that fits the threshold
            if check_square_fits(mid):
                left = mid
            else:
                right = mid - 1

        # The left pointer now points to the maximum size square that fits the threshold
        return left
        
        # m, n = len(mat), len(mat[0])
        # k = min(m, n)
        # print(m,n, k)
        # ans = 0
        # for i in range(k+1):
        #     found = False
        #     for l in range(m-i+1):
        #         total = 0
        #         for r in range(l, l + i):
        #             for c in range(i):
        #                 total += mat[r][c]
        #         if total <= threshold:
        #             found = True
        #             ans = i
        #             break                    
        #     if found is False:
        #         break
        # return ans
