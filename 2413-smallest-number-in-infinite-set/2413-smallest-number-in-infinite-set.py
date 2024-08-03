class SmallestInfiniteSet:
    # def __init__(self):
    #     self.s = SortedSet(range(1, 1001))

    # def popSmallest(self) -> int:
    #     x = self.s[0]
    #     self.s.remove(x)
    #     return x

    # def addBack(self, num: int) -> None:
    #     self.s.add(num)
    
    def __init__(self):
        self.heap = []
        self.set = set()
        for i in range(1, 1001):
            heappush(self.heap, i)
            self.set.add(i)
        

    def popSmallest(self) -> int:
        ans = heappop(self.heap)
        self.set.remove(ans)
        return ans
        

    def addBack(self, num: int) -> None:
        if num not in self.set:
            self.set.add(num)
            heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)