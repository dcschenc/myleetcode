from itertools import combinations
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return (1/2) * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
        
        pairs = combinations(points, 3)
        ans = float('-inf')
        for p1, p2, p3 in pairs:
            ans = max(ans, area(p1, p2, p3))
        return ans