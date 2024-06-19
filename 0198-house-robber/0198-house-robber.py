class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]
    
        n = len(nums)
        dp = [-1]*n
        for i, v in enumerate(nums):
            if i == 0:
                dp[0] = nums[0]
            elif i==1:
                dp[1] = nums[0] if nums[0] >= nums[1] else nums[1]
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
                # if dp[i-2] + nums[i] >= dp[i-1]:
                #     dp[i] = dp[i-2] + nums[i]
                # else:
                #     dp[i] = dp[i-1]
        return dp[-1]                
                