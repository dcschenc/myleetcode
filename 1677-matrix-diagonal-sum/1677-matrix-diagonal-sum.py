class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        m, n = len(mat), len(mat[0])
        i, j = 0, 0
        while i < m:
            ans += mat[i][j]
            i += 1
            j += 1
        i, j = 0, n-1
        while i < m:
            if i != j:
                ans += mat[i][j]
            i += 1
            j -= 1
        return ans