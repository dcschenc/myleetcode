class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1911.Maximum%20Alternating%20Subsequence%20Sum
        n = len(nums)
        dp = [[0 for j in range(2)] for i in range(n)]
        dp[0][0] = nums[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1] + nums[i], dp[i-1][0])   # even
            dp[i][1] = max(dp[i-1][0] - nums[i], dp[i-1][1])   # odd
        return max(dp[n-1])