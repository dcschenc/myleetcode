class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:      
        # s = set(nums)
        # return [x for x in range(1, len(nums) + 1) if x not in s]

        n = len(nums)    
        # Mark the presence of numbers by negating the corresponding index.
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        # Find the indices of positive values in the array.
        return [i + 1 for i in range(n) if nums[i] > 0]        
