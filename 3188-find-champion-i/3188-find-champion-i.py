class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2923.Find%20Champion%20I
        for i, row in enumerate(grid):
            if all(x == 1 for j, x in enumerate(row) if i != j):
                return i

        # m, n = len(grid), len(grid[0])
        # mx, ans = 0, 0
        # for i in range(m):
        #     if grid[i].count(1) > mx:
        #         mx = grid[i].count(1)
        #         ans = i
        # return ans
            