class MinStack:
    def __init__(self):
        self.items = []
        self.min = []

    def push(self, val: int) -> None:
        if not self.items:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)
        
        self.items.append(val)
        
    def pop(self) -> None:
        if self.items[-1] == self.min[-1]:
            self.min.pop()
        self.items.pop()
        
    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
    # def __init__(self):
    #     self.data = []
    #     # self.min_val = 

    # def push(self, val: int) -> None:
    #     if len(self.data) == 0:
    #         self.data.append((val, val))
    #     else:
    #         min_val = self.data[-1][1]
    #         if min_val > val:
    #             min_val = val
    #         self.data.append((val, min_val))

    # def pop(self) -> None:
    #     self.data.pop()

    # def top(self) -> int:
    #     return self.data[-1][0]

    # def getMin(self) -> int:
    #     return self.data[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()