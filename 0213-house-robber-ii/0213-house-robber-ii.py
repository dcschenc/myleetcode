class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRobber(nums):
            # dynamic programming - decide each problem by its sub-problems:
            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])

            return dp[-1]
        
        # edge cases:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        
        # either use first house and can't use last or last and not first:
        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))

        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        dp_first = [0] * (n-1)
        dp_first[0] = nums[0]
        dp_first[1] = max(nums[0], nums[1])

        dp_second = [0] *  (n-1)
        dp_second[0] = nums[1]
        dp_second[1] = max(nums[1], nums[2])

        for i in range(2, n-1):
            dp_first[i] = max(dp_first[i-2] + nums[i], dp_first[i-1])

        for i in range(2, n-1):
            dp_second[i] = max(dp_second[i-2] + nums[i+1], dp_second[i-1])

        # print(dp_first)
        # print(dp_second)

        return max(dp_first[-1], dp_second[-1])