class CustomStack:
    # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1381.Design%20a%20Stack%20With%20Increment%20Operation
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.inc = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        i = len(self.stack) - 1
        result = self.stack.pop() + self.inc[i]
        if i > 0:
            self.inc[i - 1] += self.inc[i]
        self.inc[i] = 0
        return result

    def increment(self, k: int, val: int) -> None:
        i = min(k, len(self.stack)) - 1
        if i >= 0:
            self.inc[i] += val
            
    # def __init__(self, maxSize: int):
    #     self.maxSize = maxSize
    #     self.stack = []        

    # def push(self, x: int) -> None:
    #     if len(self.stack) < self.maxSize:
    #         self.stack.append(x)

    # def pop(self) -> int:
    #     if self.stack:
    #         return self.stack.pop()
    #     return -1        

    # def increment(self, k: int, val: int) -> None:
    #     for i in range(k):
    #         if i > len(self.stack) - 1:
    #             break
    #         self.stack[i] += val       


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)