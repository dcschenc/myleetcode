class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
        
        # n = len(nums)
        # ans = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         ans = max(ans, (nums[i] - 1) * (nums[j] -1))
        # return ans