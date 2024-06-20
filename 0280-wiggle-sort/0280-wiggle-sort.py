class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        i, j = 1, len(nums) - 1        
        while i < n - 1:            
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i += 2
        