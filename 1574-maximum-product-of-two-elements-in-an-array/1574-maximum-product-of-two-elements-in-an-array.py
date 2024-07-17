class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return (nums[n-1] - 1) * (nums[n-2] - 1)
        
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, (nums[i] - 1) * (nums[j] -1))
        return ans