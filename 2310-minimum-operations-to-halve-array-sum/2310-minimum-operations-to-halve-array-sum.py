from heapq import heappush, heappop
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heaps = []
        total = 0
        for v in nums:
            heappush(heaps, -v)
            total += v
        reduced = 0
        steps = 0
        while reduced < total / 2:
            val = -heappop(heaps)
            val = val/2
            reduced += val
            heappush(heaps, -val)            
            steps += 1
        return steps
