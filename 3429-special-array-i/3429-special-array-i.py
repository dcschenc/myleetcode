class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for a, b in pairwise(nums):
            if (a % 2 + b % 2) in (0, 2):
                return False
        return True