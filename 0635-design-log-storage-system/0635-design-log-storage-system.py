class LogSystem:

    def __init__(self):
        self.hm = defaultdict(int)        

    def put(self, id: int, timestamp: str) -> None:
        self.hm[timestamp] = id        

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        keys = sorted(self.hm.keys())
        ans = []
        g = granularity
        if g == 'Year':
            right = 4
        elif g == 'Month':
            right = 7
        elif g == 'Day':
            right = 10
        elif g == 'Hour':
            right = 13
        elif g == 'Minute':
            right = 16
        else:
            right = 19
        
        for k in keys:
            if start[:right] <= k[:right] <= end[:right]:
                ans.append(self.hm[k])
        return ans


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)