class MyQueue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
    
    # enqueue
    def push(self, x: int) -> None:
        self.enqueue_stack.append(x)
        
    # dequeue
    def pop(self) -> int:
        # if items from dequeue stack are over refill it from enqueue stack
        if not self.dequeue_stack:
            self.fill()
            
        # otherwise pop items from dequeue stack
        return self.dequeue_stack.pop()

    def peek(self) -> int:
        if not self.dequeue_stack:
            self.fill()

        # we could use dequeue_stack[-1] operation but this is not valid
        # according to the details of this problem
        temp = self.dequeue_stack.pop()
        self.dequeue_stack.append(temp)
        return temp
    
    def empty(self) -> bool:
        return not len(self.dequeue_stack) and not len(self.enqueue_stack)
    
    # get items from enqueue to dequeue stack so we could pop items with 0(1) time
    
    def fill(self):
        while self.enqueue_stack:
            self.dequeue_stack.append(self.enqueue_stack.pop())

# Time complexity: O(1) - amortised, meaning it`s evaluated over a sequence of multiple operations.
# Space complexity: O(n)


    # def __init__(self):
    #     self.s1 = []
    #     self.s2 = []

    # def push(self, x: int) -> None:
    #     self.s1.append(x)
    #     # length = len(self.s2)
        

    # def pop(self) -> int:
    #     while self.s1:
    #         self.s2.append(self.s1.pop())
    #     res = self.s2.pop()
    #     while self.s2:
    #         self.s1.append(self.s2.pop())
    #     return res

    # def peek(self) -> int:
    #     while self.s1:
    #         self.s2.append(self.s1.pop())
    #     res = self.s2[-1]
    #     while self.s2:
    #         self.s1.append(self.s2.pop())
    #     return res

    # def empty(self) -> bool:
    #     return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()