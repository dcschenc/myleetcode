class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1139.Largest%201-Bordered%20Square
        m, n = len(grid), len(grid[0])
        down = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    down[i][j] = down[i + 1][j] + 1 if i + 1 < m else 1
                    right[i][j] = right[i][j + 1] + 1 if j + 1 < n else 1
        for k in range(min(m, n), 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if (
                        down[i][j] >= k
                        and right[i][j] >= k
                        and right[i + k - 1][j] >= k
                        and down[i][j + k - 1] >= k
                    ):
                        return k * k
        return 0


        m, n = len(grid), len(grid[0])
        dp = [[[0 for k in range(2)] for j in range(n)] for i in range(m)]
        ans = 0
        if grid[0][0] == 1: 
            dp[0][0][0] = dp[0][0][1] = 1
            ans = 1
        for i in range(1, m):
            if grid[i][0] == 1:
                dp[i][0][1] = dp[i-1][0][1] + 1
                dp[i][0][0] = 1
                ans = 1
        for j in range(1, n):
            if grid[0][j] == 1:
                dp[0][j][0] = dp[0][j-1][0] + 1
                dp[0][j][1] = 1
                ans = 1
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    dp[i][j][0] = dp[i][j-1][0] + 1
                    dp[i][j][1] = dp[i-1][j][1] + 1
                    mi = min(dp[i][j])
                    for k in range(mi-1, -1, -1):
                        if dp[i - k][j][0] >= (k + 1) and dp[i][j-k][1] >= (k + 1):
                            ans = max(ans, (k + 1) * (k+1))
                            break
        # print(dp)
        return ans
