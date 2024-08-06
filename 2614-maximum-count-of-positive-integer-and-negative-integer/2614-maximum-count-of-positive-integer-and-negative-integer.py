class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # a = sum(x > 0 for x in nums)
        # b = sum(x < 0 for x in nums)
        # return max(a, b)

        l = bisect_left(nums, 0)
        r = bisect_right(nums, 0)
        return max(l, len(nums) - r)