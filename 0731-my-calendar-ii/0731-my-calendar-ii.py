class MyCalendarTwo:
    def __init__(self):
        self.cal = defaultdict(int)

    def book(self, start: int, end: int) -> bool:  
        # if start not in self.cal:
        #     self.cal[start] = 1
        # else:
        #     self.cal[start] += 1

        # if end not in self.cal:
        #     self.cal[end] = -1
        # else:
        #     self.cal[end] -= 1

        self.cal[start] += 1
        self.cal[end] -= 1

        cnt = 0
        keys = sorted(self.cal.keys())
        for k in keys:
            # if k > end:
                # return True
            cnt += self.cal[k]
            if cnt > 2:
                self.cal[start] -= 1
                self.cal[end] += 1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)