class OrderedStream:
    def __init__(self, n: int):
        self.hm = {}
        self.n = n
        self.cur = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.hm[idKey] = value
        ans = []
        while self.cur <= self.n and self.cur in self.hm:
            ans.append(self.hm[self.cur])
            self.cur += 1
        return ans



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)