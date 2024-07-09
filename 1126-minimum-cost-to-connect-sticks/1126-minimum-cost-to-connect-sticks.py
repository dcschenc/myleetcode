import heapq
from heapq import heapify, heappop, heappush
# O(n×logn)
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            cur = heappop(sticks) + heappop(sticks)
            heappush(sticks, cur)
            cost += cur
        return cost