class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1856.Maximum%20Subarray%20Min-Product
        mod = 10 ** 9 + 7
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        stack = []
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] >= x:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
            
        presum = list(accumulate(nums, initial=0))
        return max((presum[right[i]] - presum[left[i] + 1]) * x for i, x in enumerate(nums)) % mod

        # presum = [0] * (n+1)
        # presum[0] = 0
        # for i in range(1, n+1):
        #     presum[i] = presum[i-1] + nums[i-1]
        # ans = 0
        # for i in range(n):
        #     cur = (presum[right[i]] - presum[left[i] + 1]) * nums[i] 
        #     ans = max(ans, cur)
        # return ans% mod
