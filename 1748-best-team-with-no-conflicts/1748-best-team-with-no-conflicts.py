class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1626.Best%20Team%20With%20No%20Conflicts
        pairs = list(zip(ages, scores))
        pairs.sort(key = lambda x: (x[0], x[1]))
        n = len(ages)
        dp = [0] * n
        dp[0] = pairs[0][1]
        for i in range(1, n):
            dp[i] = pairs[i][1]
            for j in range(i):
                if pairs[i][1] >= pairs[j][1] or pairs[i][0] == pairs[j][0]:
                    dp[i] = max(dp[i], dp[j] + pairs[i][1])
        return max(dp)

        # # print(pairs)
        # n = len(ages)
        # dp = [[0 for j in range(2)] for i in range(n)]
        # dp[0][1] = paris[0][1]
        # for i in range(1, n):
        #     dp[i][0] = max(dp[i-1])
        #     for j in range(i):
        #         if pairs[i][1] > pairs[j][1]:
        #             dp[i][1] = max(dp[i][1], dp[j][1])
        #         dp[i][1] = max(dp[j][0])
