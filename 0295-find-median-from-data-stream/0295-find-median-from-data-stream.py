import heapq
class MedianFinder:
    def __init__(self):    
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        heappush(self.hi, num)
        heappush(self.lo, -heappop(self.hi))
        if len(self.lo) - len(self.hi) > 1:
            heappush(self.hi, -heappop(self.lo))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (self.hi[0] - self.lo[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()