class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2711.Difference%20of%20Number%20of%20Distinct%20Values%20on%20Diagonals
        m, n = len(grid), len(grid[0])
        ans = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                left, bottom = set(), set()
                di, dj = 1, 1
                while i - di >= 0 and j - dj >= 0:
                    left.add(grid[i-di][j-dj])
                    di += 1
                    dj += 1

                di, dj = 1, 1
                while i + di < m and j + dj < n:
                    bottom.add(grid[i+di][j+dj])
                    di += 1
                    dj += 1

                ans[i][j] = abs(len(left) - len(bottom))

        return ans