class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        # https://algo.monster/liteproblems/2188
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2188.Minimum%20Time%20to%20Finish%20the%20Race
        cost = [inf] * 18
        for f, r in tires:
            i, s, t = 1, 0, f
            while t <= changeTime + f:
                s += t
                cost[i] = min(cost[i], s)
                t *= r
                i += 1

        dp = [inf] * (numLaps + 1)
        dp[0] = -changeTime
        for i in range(1, numLaps + 1):
            for j in range(1, min(18, i + 1)):
                dp[i] = min(dp[i], dp[i - j] + cost[j])
            dp[i] += changeTime
        return dp[numLaps]
