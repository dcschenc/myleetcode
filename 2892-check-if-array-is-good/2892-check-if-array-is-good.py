class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums) - 1
        return nums == [i for i in range(1, n)] + [n, n]