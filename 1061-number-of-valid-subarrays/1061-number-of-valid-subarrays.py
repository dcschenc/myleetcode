class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1063.Number%20of%20Valid%20Subarrays
        n = len(nums)
        right = [n] * n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] >= nums[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        return sum(j - i for i, j in enumerate(right))