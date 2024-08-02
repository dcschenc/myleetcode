class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def dfs(nums):
            if len(nums) == 1: return nums[0]
            if len(nums) == 2:
                return (nums[0] + nums[1]) % 10
            next_nums = []
            for i in range(1, len(nums)):
                next_nums.append((nums[i-1] + nums[i]) % 10)
            return dfs(next_nums)
        
        return dfs(nums)