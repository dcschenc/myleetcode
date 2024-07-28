class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx = max(nums)
        mi = min(nums)
        for i in range(mi, -1, -1):
            if mi % i == 0 and mx % i == 0:
                return i