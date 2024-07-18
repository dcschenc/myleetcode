class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1536.Minimum%20Swaps%20to%20Arrange%20a%20Binary%20Grid
        n = len(grid)
        # Count the number of trailing zeros in each row
        trailing_zeros = [0] * n
        for i in range(n):
            j = n - 1
            while j >= 0 and grid[i][j] == 0:
                trailing_zeros[i] += 1
                j -= 1

        # Calculate the number of swaps required
        swaps = 0
        for i in range(n):
            target = n - i - 1
            found = False
            for j in range(i, n):
                if trailing_zeros[j] >= target:
                    found = True
                    break
            if not found:
                return -1
            # Perform swaps
            while j > i:
                trailing_zeros[j], trailing_zeros[j - 1] = trailing_zeros[j - 1], trailing_zeros[j]
                j -= 1
                swaps += 1

        return swaps