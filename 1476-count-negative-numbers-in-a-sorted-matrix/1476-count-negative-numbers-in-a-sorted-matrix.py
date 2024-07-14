class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1351.Count%20Negative%20Numbers%20in%20a%20Sorted%20Matrix
        m, n = len(grid), len(grid[0])
        i, j = m - 1, 0
        ans = 0
        while i >= 0 and j < n:
            if grid[i][j] < 0:
                ans += n - j
                i -= 1
            else:
                j += 1
        return ans

        rows, cols = len(grid), len(grid[0])
        count = 0
        # Starting from the top-right corner
        r, c = 0, cols - 1  

        while r < rows and c >= 0:
            if grid[r][c] < 0:                
                count += rows - r
                c -= 1
            else:
                # Move down to the next row
                r += 1
        return count


        # m, n = len(grid), len(grid[0])
        # cnt = 0
        # i = m - 1
        # prev_j = 0
        # while i >= 0:
        #     j = prev_j
        #     while j <= n-1 and grid[i][j] >= 0:
        #         j += 1
        #     cnt += (n - j)
        #     prev_j = j
        #     i -= 1
        # return cnt
