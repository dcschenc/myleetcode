class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n//2]
        ans = 0
        for i in range(n//2):
            ans += median - nums[i]
        for i in range(n//2+1, n):
            ans += nums[i] - median
        return ans
