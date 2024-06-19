class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if len(nums) == 0:
            return [[lower, upper]]
        result = []
        start, end = -1, -1
        idx = 0        
        n = len(nums)
        if nums[0] > lower:
            result.append([lower, nums[0] - 1])
        for i in range(1, n):
            if nums[i] != nums[i-1] + 1:
                result.append([nums[i-1] + 1, nums[i] - 1])
        if nums[n-1] < upper:
            result.append([nums[n-1] + 1, upper])
        return result
