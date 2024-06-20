class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
        for j in range(left, len(nums)):
            nums[j] = 0