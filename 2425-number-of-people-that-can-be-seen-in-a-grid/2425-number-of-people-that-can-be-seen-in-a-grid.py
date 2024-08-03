class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2282.Number%20of%20People%20That%20Can%20Be%20Seen%20in%20a%20Grid
        def f(nums: List[int]) -> List[int]:
            n = len(nums)
            stk = []
            ans = [0] * n
            for i in range(n - 1, -1, -1):
                while stk and stk[-1] < nums[i]:
                    ans[i] += 1
                    stk.pop()
                if stk:
                    ans[i] += 1
                while stk and stk[-1] == nums[i]:
                    stk.pop()
                stk.append(nums[i])
            return ans

        ans = [f(row) for row in heights]
        m, n = len(heights), len(heights[0])
        for j in range(n):
            add = f([heights[i][j] for i in range(m)])
            for i in range(m):
                ans[i][j] += add[i]
        return ans