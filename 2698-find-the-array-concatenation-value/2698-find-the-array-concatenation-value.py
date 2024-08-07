class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        ans = 0
        while l < r:
            ans += int(str(nums[l]) + str(nums[r]))
            l += 1
            r -= 1
        if l == r:
            ans += nums[l]
        return ans