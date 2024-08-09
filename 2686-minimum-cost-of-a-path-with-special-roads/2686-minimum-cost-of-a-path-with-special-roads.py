
from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2662.Minimum%20Cost%20of%20a%20Path%20With%20Special%20Roads
        
        def dist(x1: int, y1: int, x2: int, y2: int) -> int:
            return abs(x1 - x2) + abs(y1 - y2)

        minheap = [(0, start[0], start[1])]
        visited = set()
        ans = inf
        while minheap:
            d, x, y = heappop(minheap)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            ans = min(ans, d + dist(x, y, *target))
            for x1, y1, x2, y2, cost in specialRoads:
                heappush(minheap, (d + dist(x, y, x1, y1) + cost, x2, y2))
        return ans


