class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
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