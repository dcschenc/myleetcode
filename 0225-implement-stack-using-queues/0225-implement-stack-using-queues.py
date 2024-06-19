from collections import deque

# class MyStack:
#     def __init__(self):
#         self.q1 = deque()
#         self.q2 = deque()

#     def push(self, x: int) -> None:
#         self.q1.append(x)

#     def pop(self) -> int:
#         while len(self.q1)>1:
#             self.q2.append(self.q1.popleft())
#         # print(self.q2)
#         res = self.q1.popleft()
#         self.q1, self.q2 = self.q2, self.q1
#         return res            

#     def top(self) -> int:
#         while len(self.q1) > 1:
#             self.q2.append(self.q1.popleft())
#         res = self.q1[0]
#         self.q2.append(self.q1.popleft())
#         self.q1, self.q2 = self.q2, self.q1
#         return res

#     def empty(self) -> bool:
#         return len(self.q1) == 0

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        res = self.q[0]
        self.push(self.q.popleft())
        return res

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()