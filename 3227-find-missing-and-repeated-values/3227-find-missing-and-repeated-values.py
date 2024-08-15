class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        total = 0
        s = set()        
        for i in range(m):
            for j in range(n):
                total += grid[i][j]
                if grid[i][j] in s:
                    twice = grid[i][j]
                s.add(grid[i][j])
        return [twice, (n*n) * (n*n + 1)//2 - total + twice]