class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2291.Maximum%20Profit%20From%20Trading%20Stocks
        n = len(present)
        dp = [[0 for j in range(budget+1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(budget + 1):
                if present[i-1] >= future[i-1] or present[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-present[i-1]] + future[i-1] - present[i-1])
                # print(i, j, dp[i][j])
        # print(dp)
        return dp[n][budget]