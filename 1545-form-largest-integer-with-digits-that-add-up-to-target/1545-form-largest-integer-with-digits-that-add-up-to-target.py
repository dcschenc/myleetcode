class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1449.Form%20Largest%20Integer%20With%20Digits%20That%20Add%20up%20to%20Target
        dp = [''] + [None] * target
        for t in range(1, target + 1):
            for d in range(9):
                if t >= cost[d] and dp[t - cost[d]] is not None:
                    candidate = str(d + 1) + dp[t - cost[d]]
                    if dp[t] is None or len(candidate) > len(dp[t]) \
                        or (len(candidate) == len(dp[t]) and candidate > dp[t]):
                        dp[t] = candidate

        return dp[target] if dp[target] is not None else "0"