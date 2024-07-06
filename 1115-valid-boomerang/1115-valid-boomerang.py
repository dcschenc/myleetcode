class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x0, y0 = points[0][0], points[0][1]
        x1, y1 = points[1][0], points[1][1]
        x2, y2 = points[2][0], points[2][1]
        return (y1-y0)*(x2-x1) != (y2-y1)*(x1-x0)