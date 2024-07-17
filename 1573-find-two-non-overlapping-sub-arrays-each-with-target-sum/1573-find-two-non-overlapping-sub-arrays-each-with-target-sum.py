class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1477.Find%20Two%20Non-overlapping%20Sub-arrays%20Each%20With%20Target%20Sum
        d = {0: 0}
        s, n = 0, len(arr)
        dp = [float('inf')] * (n + 1)
        ans = float('inf')
        for i, v in enumerate(arr, 1):
            s += v
            dp[i] = dp[i - 1]
            if s - target in d:
                j = d[s - target]
                dp[i] = min(dp[i], i - j)
                ans = min(ans, dp[j] + i - j)
            d[s] = i
        return -1 if ans > n else ans