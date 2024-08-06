class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:    
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2500.Delete%20Greatest%20Value%20in%20Each%20Row 
        for row in grid:
            row.sort()
        return sum(max(col) for col in zip(*grid))


        m, n = len(grid), len(grid[0])
        for i in range(m):
            grid[i].sort()
            
        ans = 0
        for j in range(n):
            cur = 0
            for i in range(m):
                cur = max(cur, grid[i][j])
            ans += cur
        return ans

