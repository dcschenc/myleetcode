class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        # return max(nums[:k]) - min(nums[:k])
        l, r, n = 0, k - 1, len(nums)
        diff = inf
        while r < n:
            diff = min(diff, nums[r] - nums[l] )
            r += 1
            l += 1
        return diff