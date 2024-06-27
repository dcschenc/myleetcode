class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        hm = defaultdict(int)
        ans = 0
        prev = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for k in range(j+1, n):
                        if grid[i][k] == 1:
                            ans += hm[(j, k)]
                            hm[(j, k)] += 1
        return ans

        # def count(i, j):
        #     cnt = 0
        #     for x in range(i+1, m):
        #         for y in range(j+1, n):
        #             if grid[x][y] == 1 and grid[i][y] == 1 and grid[x][j] == 1:
        #                 cnt += 1            
        #     return cnt
        # m, n = len(grid), len(grid[0])
        # ans = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             ans += count(i, j)
        # return ans
