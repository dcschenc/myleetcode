class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for num in nums:
            if num < 0:
                return -1
            if -num in nums:
                return num
        return -1