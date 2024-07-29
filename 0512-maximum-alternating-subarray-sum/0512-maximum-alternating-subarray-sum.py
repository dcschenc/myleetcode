class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2036.Maximum%20Alternating%20Subarray%20Sum
        n = len(nums)
        if n == 1: return nums[0]
        dp = [[0 for j in range(2)] for i in range(n)]
        dp[0][0] = nums[0]
        dp[0][1] = 0
        ans = -float(inf)
        ans = max(ans, max(dp[0]))
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1] + nums[i], nums[i])
            dp[i][1] = max(dp[i-1][0] - nums[i], 0)
            ans = max(ans, max(dp[i]))
        return ans