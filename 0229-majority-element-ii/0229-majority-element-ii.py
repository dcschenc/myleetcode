class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = set()
        n = len(nums)
        for i, num in enumerate(nums):
            if i + n//3 < n and nums[i + n//3] == num:
                result.add(num)
        return result