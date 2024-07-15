class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        min_rows, max_cols = [], []
        for i in range(m):
            min_rows.append(min(matrix[i]))
        for j in range(n):
            max_cols.append(max([matrix[i][j] for i in range(m)]))
        ans = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == min_rows[i] == max_cols[j]:
                    ans.append(matrix[i][j])
        return ans
