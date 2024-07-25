# from sortedcontainers import SortedList
class SeatManager:
    # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1845.Seat%20Reservation%20Manager
    def __init__(self, n: int):
        self.n = n
        self.available = []
        for i in range(1, n + 1):
            heappush(self.available, i)

    def reserve(self) -> int:
        num = heappop(self.available)
        return num        

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.available, seatNumber)

    # def __init__(self, n: int):
    #     self.n = n
    #     self.available = SortedList()
    #     self.reserves = set()
    #     for i in range(1, n + 1):
    #         self.available.add(i)        

    # def reserve(self) -> int:
    #     num = self.available[0]
    #     self.reserves.add(num)
    #     self.available.remove(num)
    #     return num        

    # def unreserve(self, seatNumber: int) -> None:
    #     self.reserves.discard(seatNumber)
    #     self.available.add(seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)