class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        n, m = len(points), len(queries)
        ans = [0] * m
        for i, (x1, y1, r) in enumerate(queries):
            for x2, y2 in points:
                if math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= r:
                    ans[i] += 1
        return ans