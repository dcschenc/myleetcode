class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        onesrow, onescol, zerosrow, zeroscol = Counter(), Counter(), Counter(), Counter()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    onesrow[r] += 1
                    onescol[c] += 1
                else:
                    zerosrow[r] += 1
                    zeroscol[c] += 1

        diff = [[0 for j in range(n)] for i in range(m)]
        for r in range(m):
            for c in range(n):
                diff[r][c] = onesrow[r] + onescol[c] - zerosrow[r] - zeroscol[c]
        return diff
