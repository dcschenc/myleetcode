class MyCalendar:

    def __init__(self):
        self.cal = []        

    def book(self, start: int, end: int) -> bool:
        if len(self.cal) == 0:
            self.cal.append((start, end))
            return True
        idx = bisect_right([s for s, d in self.cal], start)
        conflict = False
        if idx == 0:
            if end > self.cal[idx][0]:
                conflict = True
        elif idx == len(self.cal):
            if start < self.cal[idx-1][1]:
                conflict = True
        else:
            if start < self.cal[idx-1][1] or end > self.cal[idx][0]:
                conflict = True
        if conflict:
            return False
        self.cal.append((start, end))
        self.cal.sort(key=lambda x:x[0])
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)