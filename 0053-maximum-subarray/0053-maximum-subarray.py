class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float(inf)] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)

        # n = len(nums)
        # max_num = -10**4-1
        # curr = 0
        # for i in range(n):
        #     curr += nums[i]
        #     if curr > max_num:
        #         max_num = curr
        #     if curr < 0:
        #         curr = 0
        # return max_num
