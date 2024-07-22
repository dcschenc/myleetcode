class FrontMiddleBackQueue:
    # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1670.Design%20Front%20Middle%20Back%20Queue
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val: int) -> None:
        self.left.append(val)
        self.rebalance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.rebalance()

    def popFront(self) -> int:
        if not self.left and not self.right:
            return -1
        if self.left:
            val = self.left.popleft()
        else:
            val = self.right.popleft()
        self.rebalance()
        return val

    def popMiddle(self) -> int:
        if not self.left and not self.right:
            return -1
        if len(self.left) == len(self.right):
            val = self.left.pop()
        else:
            val = self.right.popleft()
        self.rebalance()
        return val

    def popBack(self) -> int:
        if not self.right:
            return -1
        val = self.right.pop()
        self.rebalance()
        return val

    def rebalance(self):
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        if len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()