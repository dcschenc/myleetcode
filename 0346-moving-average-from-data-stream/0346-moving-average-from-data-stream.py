from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.pre_sum = 0
        

    def next(self, val: int) -> float:
        if len(self.queue) < self.size:
            self.pre_sum += val
            self.queue.append(val)
        else:
            last_val = self.queue.popleft()     
            self.queue.append(val)              
            self.pre_sum = self.pre_sum - last_val + val
        
        return self.pre_sum /len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)