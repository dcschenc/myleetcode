class Solution:
    def strangePrinter(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0600-0699/0664.Strange%20Printer
        @cache
        def dp(i, j):
            if i == j:
                return 1
            if s[i] == s[j]:
                return dp(i, j - 1)
            ans = float('inf')
            for k in range(i, j):
                ans = min(ans, dp(i, k) + dp(k + 1, j))
            return ans

        return dp(0, len(s) - 1)

        n = len(s)
        return dp[0][n-1]
        n = len(s)
        dp = [[inf] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        return dp[0][-1]