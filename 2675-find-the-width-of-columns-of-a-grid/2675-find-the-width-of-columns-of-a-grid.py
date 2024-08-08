class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max(len(str(x)) for x in col) for col in zip(*grid)]
        
        m, n = len(grid), len(grid[0])
        ans = []
        for j in range(n):
            ans.append(max(len(str(grid[i][j])) for i in range(m)))
        return ans