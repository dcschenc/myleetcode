class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mi = nums[0] + 1
        i, n = 1, len(nums)
        total = 0
        while i < n:
            if nums[i] < mi:
                total += mi - nums[i]
                nums[i] = mi
            mi = nums[i] + 1
            i += 1
        return total

        
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                ans += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        return ans