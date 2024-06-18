class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:        
        # the key is to add 0 to the end of heights and -1 to the stack
        heights.append(0)
        stack = [-1]  ## to store index
        result = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = (i - 1) - stack[-1]
                result = max(result, h * w)
            stack.append(i)
        return result
    
        # # heights = [2,1,5,6,2,3]
        # stack = []
        # max_area = 0
        # for i, h in enumerate(heights):
        #     # if not stack or h >= heights[stack[-1]]:
        #     #     stack.append(i)
        #     # else:
        #     while stack and h<=heights[stack[-1]]:
        #         idx = stack.pop()
        #         if (i-idx)*heights[idx] > max_area:
        #             max_area = (i-idx)*heights[idx]
        #     stack.append(i)
        # print(stack)
        # if stack:            
        #     # i = len(stack)
        #     # if heights[i] > max_area:
        #     #     max_area = heights[i]
        #     count = 1
        #     while stack:
        #         idx = stack.pop()
        #         if count*heights[idx] >= max_area:
        #             max_area = count*heights[idx]
        #         count+=1
        # return max_area
            
        