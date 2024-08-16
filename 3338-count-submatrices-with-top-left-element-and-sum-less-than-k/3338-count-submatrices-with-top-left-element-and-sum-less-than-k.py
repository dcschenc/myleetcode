class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3070.Count%20Submatrices%20with%20Top-Left%20Element%20and%20Sum%20Less%20Than%20k
        s = [[0] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]
        ans = 0
        for i, row in enumerate(grid, 1):
            for j, x in enumerate(row, 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + x
                ans += s[i][j] <= k
        return ans