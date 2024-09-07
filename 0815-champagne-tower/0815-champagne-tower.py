class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * 101 for _ in range(101)]
        dp[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    half = (dp[i][j] - 1) / 2
                    dp[i][j] = 1
                    dp[i + 1][j] += half
                    dp[i + 1][j + 1] += half
        return dp[query_row][query_glass]

        # n = 101
        # dp = [[0 for j in range(n)] for i in range(n)]
        # dp[1][1] = poured
        # for i in range(2, n):
        #     for j in range(1, i + 1):
        #         if dp[i-1][j] > 1:
        #             dp[i][j] += (dp[i-1][j] - 1)/2
        #         if dp[i-1][j-1] > 1:
        #             dp[i][j] += (dp[i-1][j-1] - 1)/2
        # # print(dp)
        # return dp[query_row + 1][query_glass + 1] if dp[query_row + 1][query_glass + 1] < 1 else 1
