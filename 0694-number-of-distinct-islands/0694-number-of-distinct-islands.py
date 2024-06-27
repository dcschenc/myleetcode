class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i, j, path, level):
            grid[i][j] = 0
            if i - 1 >= 0 and grid[i-1][j] == 1:
                path = dfs(i-1, j, path + f'{level}u', level + 1)
            if i + 1 <= m - 1 and grid[i+1][j] == 1:
                path = dfs(i + 1, j, path + f'{level}d', level + 1)
            if j - 1 >= 0 and grid[i][j-1] == 1:
                path = dfs(i, j - 1, path + f'{level}l', level + 1)
            if j + 1 <= n - 1 and grid[i][j+1] == 1:
                path = dfs(i, j + 1, path + f'{level}r', level + 1)
            return path

        islands = defaultdict(int)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = dfs(i, j, '', 1)
                    islands[path] += 1
        # print(islands)
        return len(islands)