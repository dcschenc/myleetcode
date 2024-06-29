class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # there are two cases:
        # case 1: the max array happens without need to cross boundary
        # case 2: the max array happens with crossing boundary
        #       In this case, the problem is equal to total sum - min_sum array within one length
        L = len(nums)
        dp = [-math.inf] * L
        dp[0] = nums[0]
        for i in range(1, L):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        max_nc = max(dp)
        # print(dp)

        dp[0] = nums[0]
        for i in range(1, L):
            dp[i] = min(dp[i - 1] + nums[i], nums[i])
        max_c = sum(nums) - min(dp)
        if max_c == 0: # special case where the whole array is used
            return max_nc

        return max(max_nc, max_c)


        cur_min, cur_max = 0, 0
        glb_min, glb_max = nums[0], nums[0]
        total = 0
        for i in range(len(nums)):
            cur_min = min(cur_min + nums[i], nums[i])
            cur_max = max(cur_max + nums[i], nums[i])
            glb_min = min(glb_min, cur_min)
            glb_max = max(glb_max, cur_max)
            total += nums[i]
        
        return max(total - glb_min, glb_max) if glb_max > 0 else glb_max