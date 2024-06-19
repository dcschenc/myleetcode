class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        i, n = 1, len(nums)
        while i < n:
            ans ^= nums[i]
            i += 1
        return ans