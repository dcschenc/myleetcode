class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        # # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1434.Number%20of%20Ways%20to%20Wear%20Different%20Hats%20to%20Each%20Other
        # g = defaultdict(list)
        # for i, h in enumerate(hats):
        #     for v in h:
        #         g[v].append(i)
        # mod = 10**9 + 7
        # n = len(hats)
        # m = max(max(h) for h in hats)
        # f = [[0] * (1 << n) for _ in range(m + 1)]
        # f[0][0] = 1
        # for i in range(1, m + 1):
        #     for j in range(1 << n):
        #         f[i][j] = f[i - 1][j]
        #         for k in g[i]:
        #             if j >> k & 1:
        #                 f[i][j] = (f[i][j] + f[i - 1][j ^ (1 << k)]) % mod
        # return f[m][-1]
        
        mod = 10**9 + 7
        n = len(hats)

        # Create a list of people who like each hat
        hat_to_people = defaultdict(list)
        for person, hat_list in enumerate(hats):
            for hat in hat_list:
                hat_to_people[hat].append(person)

        # dp[mask] will be the number of ways to assign hats to people represented by mask
        dp = [0] * (1 << n)
        dp[0] = 1

        for hat in range(1, 41):
            if hat not in hat_to_people:
                continue

            # Traverse the dp array from right to left to avoid using the same hat in the same iteration
            for mask in range((1 << n) - 1, -1, -1):
                for person in hat_to_people[hat]:
                    if mask & (1 << person) == 0:
                        dp[mask | (1 << person)] = (dp[mask | (1 << person)] + dp[mask]) % mod

        return dp[(1 << n) - 1]

