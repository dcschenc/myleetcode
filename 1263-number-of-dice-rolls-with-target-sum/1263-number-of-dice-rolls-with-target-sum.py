class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1155.Number%20of%20Dice%20Rolls%20With%20Target%20Sum
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        mod = 10**9 + 7
        for i in range(1, n + 1):
            for j in range(1, min(i * k, target) + 1):
                for h in range(1, min(j, k) + 1):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - h]) % mod
        return dp[n][target]


        # dp = [[0 for j in range(target + 1)] for i in range(n + 1) ]
        # for m in range(1, k + 1):
        #     if m == target + 1: break
        #     dp[1][m] = 1
        # for i in range(1, n + 1):
        #     for j in range(target + 1):
        #         for m in range(1, k + 1):
        #             if j - m < 0: break
        #             dp[i][j] += dp[i-1][j-m]
        # return dp[n][target] % (10 ** 9 + 7)