class Solution:
    def minimumSum(self, nums: List[int]) -> int:    
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2908.Minimum%20Sum%20of%20Mountain%20Triplets%20I    
        n = len(nums)
        ans = float('inf')
        left, right = [float('inf')] * n, [float('inf')] * n
        for i in range(1, n):
            left[i] = min(left[i - 1], nums[i - 1])
        for i in range(n-2, -1, -1):
            right[i] = min(right[i + 1], nums[i + 1])
        for i in range(1, n-1):
            if nums[i] > left[i] and nums[i] > right[i]:
                ans = min(ans, nums[i] + left[i] + right[i])
        return ans if ans != float('inf') else -1
        
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             if nums[j] > nums[i] and nums[j] > nums[k]:
        #                 ans = min(ans, nums[i] + nums[j] + nums[k])
        # return ans if ans != float('inf') else -1
