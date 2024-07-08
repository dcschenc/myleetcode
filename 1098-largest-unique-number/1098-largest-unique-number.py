class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i-1]:
                continue
            if i + 1 < len(nums) and nums[i] == nums[i+1]:
                continue
            return nums[i]               
        return -1
