class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2907.Maximum%20Profitable%20Triplets%20With%20Increasing%20Prices%20I
        n = len(prices)
        ans = -1
        for j, x in enumerate(profits):
            left = right = 0
            for i in range(j):
                if prices[i] < prices[j] and left < profits[i]:
                    left = profits[i]
            for k in range(j + 1, n):
                if prices[j] < prices[k] and right < profits[k]:
                    right = profits[k]
            if left and right:
                ans = max(ans, left + x + right)
        return ans

        # n = len(prices)
        # dp = [[-1 for j in range(3)] for i in range(n)]
        # ans = -1
        # for i in range(n):
        #     dp[i][0] = profits[i]
        #     for j in range(i):
        #         if prices[i] > prices[j]:
        #             dp[i][1] = max(dp[i][1], profits[i] + profits[j])
        #             if dp[j][1] != -1:
        #                 dp[i][2] = max(dp[i][2], dp[j][1] + profits[i])
        #                 ans = max(ans, dp[i][2])
        # return ans

        