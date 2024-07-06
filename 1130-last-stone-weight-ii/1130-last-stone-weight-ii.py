class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1049.Last%20Stone%20Weight%20II
        # https://algo.monster/liteproblems/1049

        s = sum(stones)
        m, n = len(stones), s >> 1
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if stones[i - 1] <= j:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1])
        return s - 2 * dp[-1][-1]


        # total_sum = sum(stones)
        # n = len(stones)

        # dp = [False] * (total_sum // 2 + 1)
        # dp[0] = True

        # for stone in stones:
        #     for j in range(total_sum // 2, stone - 1, -1):
        #         dp[j] |= dp[j - stone]

        # for j in range(total_sum // 2, -1, -1):
        #     if dp[j]:
        #         return total_sum - 2 * j

        # return total_sum