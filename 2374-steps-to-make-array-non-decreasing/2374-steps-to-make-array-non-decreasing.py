class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2289.Steps%20to%20Make%20Array%20Non-decreasing
        stack, n = [], len(nums)
        dp = [0] * n
        for i in range(n-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i] + 1, dp[stack.pop()])            
            stack.append(i)
        return max(dp)