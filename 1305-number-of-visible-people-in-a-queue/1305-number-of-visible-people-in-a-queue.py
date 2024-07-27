class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1944.Number%20of%20Visible%20People%20in%20a%20Queue
        n = len(heights)
        ans = [0] * n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and stk[-1] < heights[i]:
                ans[i] += 1
                stk.pop()
            if stk:
                ans[i] += 1
            stk.append(heights[i])
        return ans