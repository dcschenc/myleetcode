class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1762.Buildings%20With%20an%20Ocean%20View
        ans = []
        mx = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > mx:
                ans.append(i)
                mx = heights[i]
        return ans[::-1]

        # stack = []
        # for i, h in enumerate(heights):
        #     while stack and h >= stack[-1][0]:
        #         stack.pop()
        #     stack.append((h, i))
        # return [x[1] for x in stack]

        max_h = -float('inf')
        i = len(heights) - 1
        res = []
        while i >= 0:
            if heights[i] > max_h:
                res.append(i)
                max_h = heights[i]
            # max_h = max(max_h, heights[i])
            i -= 1
        res.reverse()
        return res