class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def dfs(r, c):
            dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            max_path = 1
            for i, j in dr:
                new_r, new_c = r + i, c + j
                if 0 <= new_r <= m-1 and 0 <= new_c <= n-1 and matrix[new_r][new_c] > matrix[r][c]:
                    max_path = max(max_path, 1 + dfs(new_r, new_c))
            return max_path
            

        result = 0
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                result = max(result, dfs(r, c))
        return result

