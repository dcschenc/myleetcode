class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1444.Number%20of%20Ways%20of%20Cutting%20a%20Pizza
        @cache
        def dfs(i: int, j: int, k: int) -> int:
            if k == 0:
                return int(s[m][n] - s[i][n] - s[m][j] + s[i][j] > 0)
            ans = 0
            for x in range(i + 1, m):
                if s[x][n] - s[i][n] - s[x][j] + s[i][j] > 0:
                    ans += dfs(x, j, k - 1)
            for y in range(j + 1, n):
                if s[m][y] - s[i][y] - s[m][j] + s[i][j] > 0:
                    ans += dfs(i, y, k - 1)
            return ans % mod

        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(pizza, 1):
            for j, c in enumerate(row, 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + int(c == 'A')

        return dfs(0, 0, k - 1)

        rows = len(pizza)
        cols = len(pizza[0])
        apples = [[0] * (cols + 1) for row in range(rows + 1)]
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                apples[row][col] = ((pizza[row][col] == 'A')
                                    + apples[row + 1][col]
                                    + apples[row][col + 1]
                                    - apples[row + 1][col + 1])
        dp = [[[0 for col in range(cols)] for row in range(rows)] for remain in range(k)]
        dp[0] = [[int(apples[row][col] > 0) for col in range(cols)]
             for row in range(rows)]
        mod = 10 ** 9 + 7
        for remain in range(1, k):
            for row in range(rows):
                for col in range(cols):
                    val = 0
                    for next_row in range(row + 1, rows):
                        if apples[row][col] - apples[next_row][col] > 0:
                            val += dp[remain - 1][next_row][col]
                    for next_col in range(col + 1, cols):
                        if apples[row][col] - apples[row][next_col] > 0:
                            val += dp[remain - 1][row][next_col]
                    dp[remain][row][col] = val % mod
        return dp[k - 1][0][0]


        @cache
        def dfs(r, c, cut):
            if cut == 0:
                return 1 if dp[r][c] > 0 else 0
            ans = 0
            has_apple = False
            for i in range(r+1, m):
                # if dp[r][c] - dp[i][c] > 0:
                if has_apple or 'A' in pizza[i-1][c:]:
                    has_apple = True
                    ans += dfs(i, c, cut - 1)
            has_apple = False
            for j in range(c+1, n):
                # if dp[r][c] - dp[r][j] > 0:
                if has_apple or 'A' in [pizza[x][j-1] for x in range(r, m)]:
                    has_apple = True
                    ans += dfs(r, j, cut - 1)
            return ans

        m, n = len(pizza), len(pizza[0])
        dp = [[0]* (n+1) for _ in range(m+1)]

        # dp[r][c]: the total number of apples can collect from r-> m and c -> n
        # the dp[r+1][c] and dp[r][c+1] are overlapping at dp[i+1][j+1] 
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1] - dp[i+1][j+1] + int(pizza[i][j] == 'A')
        
        return dfs(0, 0, k - 1)% (10**9+7)
