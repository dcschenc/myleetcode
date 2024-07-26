class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # Use a binary search on columns to efficiently find a peak element.
        # For each column considered, find the global maximum in that column.
        # Compare this maximum element with its neighbors. If it is greater than its neighbors, it's a peak. If not, move towards the direction of the higher neighbor.
        def get_max_index(col):
            max_row = 0
            for row in range(len(mat)):
                if mat[row][col] > mat[max_row][col]:
                    max_row = row
            return max_row

        left, right = 0, len(mat[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            max_row = get_max_index(mid)
            
            if mid > 0 and mat[max_row][mid] < mat[max_row][mid - 1]:
                right = mid - 1
            elif mid < len(mat[0]) - 1 and mat[max_row][mid] < mat[max_row][mid + 1]:
                left = mid + 1
            else:
                return [max_row, mid]

        # l, r = 0, len(mat) - 1
        # while l < r:
        #     mid = (l + r) >> 1
        #     j = mat[mid].index(max(mat[mid]))
        #     if mat[mid][j] > mat[mid + 1][j]:
        #         r = mid
        #     else:
        #         l = mid + 1
        # return [l, mat[l].index(max(mat[l]))]
        
        # m, n = len(mat), len(mat[0])        
        # for i in range(m):
        #     for j in range(n):
        #         if all(mat[i][j] > mat[x][y] for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]\
        #          if 0 <= x <= m-1 and 0 <= y <= n-1):
        #             return [i, j]
        

