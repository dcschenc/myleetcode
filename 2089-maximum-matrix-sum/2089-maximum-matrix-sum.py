class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1975.Maximum%20Matrix%20Sum
        m, n = len(matrix), len(matrix[0])
        mi, total, cnt = float('inf'), 0, 0
        for i in range(m):
            for j in range(n):
                cur = abs(matrix[i][j])
                mi = min(mi, cur)
                total += cur
                if matrix[i][j] < 0:
                    cnt += 1
        if cnt % 2 == 0:
            return total
        return total - 2 * mi