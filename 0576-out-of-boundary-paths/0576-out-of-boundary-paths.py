class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # https://leetcode.com/problems/out-of-boundary-paths/solutions/2288937/dp-memoization-solution/            
        @cache
        def dfs(i, j, move):
            if i >= m or i < 0 or j >= n or j < 0:
                return 1
            if move == 0:
                return 0
            ans = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                # if (x, y) in visited:
                    # continue
                ans += dfs(x, y, move - 1)
                # visited.add((x, y))
            return ans
        # visited = set()
        # visited.add((startRow, startColumn))
        return dfs(startRow, startColumn, maxMove) % (10 ** 9 + 7)