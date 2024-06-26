class MyCircularQueue:
    # https://leetcode.com/problems/design-circular-queue/
    def __init__(self, k: int):
        self.capacity = k
        self.queue = [None] * k
        self.front = 0
        self.rear = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
        
        # if self.isEmpty():
        #     return False
        # if self.head == self.tail and self.size == 1:
        #     return True
        # if self.head - self.tail == 1 or self.tail - self.head + 1 == self.size:
        #     return True
#         if self.head < self.tail:
#             if self.tail - self.head + 1 == self.size:
#                 return True
#             else:
#                 return False
#         elif self.head == self.tail and self.size == 1 :
#             return True
            
#         elif self.tail + 1 == self.head:
#             return True
        # return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()