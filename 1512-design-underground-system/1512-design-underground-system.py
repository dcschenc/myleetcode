class UndergroundSystem:
    # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1396.Design%20Underground%20System
    def __init__(self):
        self.travels = {}
        self.times = defaultdict(tuple)        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travels[id] = (stationName, t)        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, start_t = self.travels[id]
        k = start + '_' + stationName
        if k in self.times:
            total, av = self.times[k]
            time = total * av + (t - start_t)
            total += 1
        else:
            time = t - start_t
            total = 1
        av = time / total
        self.times[k] = (total, av)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        k = startStation + '_' + endStation
        return self.times[k][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)