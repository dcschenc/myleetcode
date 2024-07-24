class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mi = float('inf')
        ans = -1
        for i, (x2, y2) in enumerate(points):
            if (x2 == x or y2 == y) and abs(x2 - x) + abs(y2 - y) < mi:
                mi = abs(x2 - x) + abs(y2 - y)
                ans = i
        return ans