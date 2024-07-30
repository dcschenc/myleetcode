class RangeFreqQuery:
    # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2080.Range%20Frequency%20Queries
    def __init__(self, arr: List[int]):
        self.hm = defaultdict(list)
        for i, num in enumerate(arr):
            self.hm[num].append(i)        

    def query(self, left: int, right: int, value: int) -> int:
        if self.hm[value] == 0:
            return 0
        l = bisect_left(self.hm[value], left)
        r = bisect_right(self.hm[value], right)
        return r - l
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)