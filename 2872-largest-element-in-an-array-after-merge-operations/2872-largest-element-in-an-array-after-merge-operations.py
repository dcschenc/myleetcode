class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/
        if len(nums) == 1:
            return nums[0]
        ans = 0
        n = len(nums)
        right = n - 1
        while right >= 1:
            if nums[right-1] <= nums[right]:
                nums[right-1] = nums[right-1] + nums[right]
            ans = max(ans, nums[right-1])
            # else:                
            #     ans = max(ans, nums[right-1])
            right = right - 1
        return ans