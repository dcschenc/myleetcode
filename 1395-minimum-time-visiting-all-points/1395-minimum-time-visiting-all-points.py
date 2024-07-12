class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            target_x, target_y = points[i + 1]
            ans += max(abs(target_x - curr_x), abs(target_y - curr_y))
        
        return ans
        
        # n = len(points)
        # ans = 0        
        # for i in range(n-1):
        #     x0, y0 = points[i]
        #     x1, y1 = points[i+1] 
        #     if x1 >= x0:
        #         if x1 - x0 < y1 - y0:                    
        #             ans += y1 - y0
        #         else:
        #             ans += x1 - x0
        #     else:
        #         if x0 - x1 < y0 - y1:
        #             ans += y0 - y1
        #         else:
        #             ans += x0 - x1
        # return ans