class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
        return max(dp)
        
        if not nums:
            return 0
        cur, max_l = 1,1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
                max_l = max(max_l, cur)
            else:
                cur = 1
        return max_l

        # n = len(nums)
        # start = 0
        # max_l = 1
        # for i in range(1,n):
        #     # if i == 0:
        #     #     max_l = 1
        #     # else:
        #     if nums[i] > nums[i-1]:
        #         if i-start + 1 > max_l:
        #             max_l = i-start + 1
        #     else:
        #         start = i
        # return max_l