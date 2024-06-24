class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:      
        n = len(nums)    
        # Mark the presence of numbers by negating the corresponding index.
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        # Find the indices of positive values in the array.
        disappeared = [i + 1 for i in range(n) if nums[i] > 0]        
        return disappeared

        # n = len(nums)
    
        # # Cyclic sort to rearrange the numbers
        # for i in range(n):
        #     while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
        #         nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # # Find missing numbers
        # missing_numbers = []
        # for i in range(n):
        #     if nums[i] != i + 1:
        #         missing_numbers.append(i + 1)

        # return missing_numbers