class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        s = set(nums)
        return len(s) == len(nums) and min(nums) + len(s) - 1 == max(nums)