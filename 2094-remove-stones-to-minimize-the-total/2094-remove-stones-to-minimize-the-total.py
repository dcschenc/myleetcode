from heapq import heappush, heappop, heapify
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heaps = []
        for i in range(len(piles)):
            heappush(heaps, -piles[i])
        while k > 0:
            val = -heappop(heaps)
            val = val - val//2
            heappush(heaps, -val)
            k -= 1
        return -sum(heaps)
        