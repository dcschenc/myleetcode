class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        ax = [ax1, ax2]
        bx = [bx1, bx2]
        ay = [ay1, ay2]
        by = [by1, by2]
        # if bx1 > ax2 or bx2 < ax1: return 0
        w = max(0, min(ax2, bx2) - max(ax1, bx1))
        h = max(0, min(ay2, by2) - max(ay1, by1))
        total = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        return total - w * h