class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:        
        # def backtrack(x, y, cur):
        #     ans[0] = max(ans[0], cur)
        #     for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        #         new_x, new_y = x + dx, y + dy
        #         if 0 <= new_x <= m-1 and 0 <= new_y <= n-1 and visited[(new_x, new_y)] is False and grid[new_x][new_y] != 0:
        #             visited[(new_x, new_y)] = True
        #             backtrack(new_x, new_y, cur + grid[new_x][new_y])
        #             visited[(new_x, new_y)] = False
        # m, n, ans = len(grid), len(grid[0]), [0]
        # visited = defaultdict(bool)
        # for i in range(m):
        #     for j in range(n):
        #         backtrack(i, j, 0)
        # return ans[0]

        def dfs(i: int, j: int) -> int:
            if not (0 <= i < m and 0 <= j < n and grid[i][j]):
                return 0
            v = grid[i][j]
            grid[i][j] = 0
            ans = max(dfs(i + a, j + b) for a, b in pairwise(dirs)) + v
            grid[i][j] = v
            return ans

        m, n = len(grid), len(grid[0])
        dirs = (-1, 0, 1, 0, -1)
        return max(dfs(i, j) for i in range(m) for j in range(n))

        