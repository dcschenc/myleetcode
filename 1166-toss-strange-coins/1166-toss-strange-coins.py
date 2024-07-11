class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1230.Toss%20Strange%20Coins
        # @cache
        # def dp(i, k):
        #     if k == 0:
        #         p = 1
        #         for j in range(i + 1):
        #             p *= (1 - prob[j])
        #         return p

        #     if i == 0:
        #         if k > 1:
        #             return 0
        #         else:
        #             return prob[0]

        #     return dp(i - 1, k) * (1 - prob[i]) + dp(i - 1, k - 1) * prob[i]
        
        # n = len(prob)
        # return dp(n-1, target)

        n = len(prob)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i, p in enumerate(prob, 1):
            for j in range(min(i, target) + 1):
                dp[i][j] = (1 - p) * dp[i - 1][j]
                if j:
                    dp[i][j] += p * dp[i - 1][j - 1]
        return dp[n][target]