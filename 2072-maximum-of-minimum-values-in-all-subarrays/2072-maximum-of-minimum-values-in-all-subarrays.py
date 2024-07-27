class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1950.Maximum%20of%20Minimum%20Values%20in%20All%20Subarrays
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        stk = []
        for i, x in enumerate(nums):
            while stk and nums[stk[-1]] >= x:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] >= nums[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        ans = [0] * n
        for i in range(n):
            m = right[i] - left[i] - 1
            ans[m - 1] = max(ans[m - 1], nums[i])
        for i in range(n - 2, -1, -1):
            ans[i] = max(ans[i], ans[i + 1])
        return ans

        # n = len(nums)    
        # ans = []    
        # for size in range(1, n + 1):
        #     cur_max = 0
        #     prev = float('inf')
        #     for i in range(n):
        #         if i + size > n:
        #             break
        #         if i == 0:
        #             prev = min(nums[:size])
        #         else:
        #             if nums[i-1] == prev:
        #                 prev = min(nums[i:i+size])
        #             else:
        #                 prev = min(prev, nums[i+size-1])
        #         cur_max = max(cur_max, prev)
        #     ans.append(cur_max)
        # return ans