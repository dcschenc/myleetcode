class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(max(nums) + 1):
            idx = bisect_left(nums, x)
            if len(nums) - idx == x:
                return x
        return -1