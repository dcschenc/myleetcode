class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        idx = nums.index(min(nums))
        nums = nums[idx:] + nums[:idx]
        for i, num in enumerate(nums):
            if i > 0 and num < nums[i-1]:
                return -1
        return len(nums) - idx if idx != 0 else 0