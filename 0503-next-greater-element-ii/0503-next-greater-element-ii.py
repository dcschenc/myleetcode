class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/0500-0599/0503.Next%20Greater%20Element%20II
        n = len(nums)
        ans = [-1] * n
        stk = []
        for i in range(n * 2 - 1, -1, -1):
            i %= n
            while stk and stk[-1] <= nums[i]:
                stk.pop()
            if stk:
                ans[i] = stk[-1]
            stk.append(nums[i])
        return ans


        next_greater = {}
        stack = []
        for num in nums:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        for num in nums[::-1]:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        result = [next_greater.get(num, -1) for num in nums]
        return result
        