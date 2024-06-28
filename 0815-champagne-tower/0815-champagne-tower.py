class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        f = [[0] * 101 for _ in range(101)]
        f[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                if f[i][j] > 1:
                    half = (f[i][j] - 1) / 2
                    f[i][j] = 1
                    f[i + 1][j] += half
                    f[i + 1][j + 1] += half
        return f[query_row][query_glass]

        n = 101
        dp = [[0 for j in range(n)] for i in range(n)]
        dp[1][1] = poured
        for i in range(2, n):
            for j in range(1, i + 1):
                if dp[i-1][j] > 1:
                    dp[i][j] += (dp[i-1][j] - 1)/2
                if dp[i-1][j-1] > 1:
                    dp[i][j] += (dp[i-1][j-1] - 1)/2
        # print(dp)
        return dp[query_row + 1][query_glass + 1] if dp[query_row + 1][query_glass + 1] < 1 else 1
