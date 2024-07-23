class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        w = []
        for x, y in rectangles:
            w.append(min(x, y))
        mx = max(w)
        return w.count(mx)