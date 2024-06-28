from sortedcontainers import SortedList

class ExamRoom:
    def __init__(self, n: int):
        def dist(x):
            l, r = x
            return r - l - 1 if l == -1 or r == n else (r - l) >> 1

        self.n = n
        self.ts = SortedList(key=lambda x: (-dist(x), x[0]))
        self.left = {}
        self.right = {}
        self.add((-1, n))

    def seat(self) -> int:
        s = self.ts[0]
        p = (s[0] + s[1]) >> 1
        if s[0] == -1:
            p = 0
        elif s[1] == self.n:
            p = self.n - 1
        self.delete(s)
        self.add((s[0], p))
        self.add((p, s[1]))
        return p

    def leave(self, p: int) -> None:
        l, r = self.left[p], self.right[p]
        self.delete((l, p))
        self.delete((p, r))
        self.add((l, r))

    def add(self, s):
        self.ts.add(s)
        self.left[s[1]] = s[0]
        self.right[s[0]] = s[1]

    def delete(self, s):
        self.ts.remove(s)
        self.left.pop(s[1])
        self.right.pop(s[0])

    # def dist(self, x, y):  # length of the interval (x, y)
    #     if x == -1:        # note here we negate the value to make it maxheap
    #         return -y
    #     elif y == self.N:
    #         return -(self.N - 1 - x)
    #     else:
    #         return -(abs(x-y)//2) 
        
    # def __init__(self, N):
    #     self.N = N
    #     self.pq = [(self.dist(-1, N), -1, N)]  # initialize heap
        
    # def seat(self):
    #     _, x, y = heapq.heappop(self.pq)  # current max interval 
    #     if x == -1:
    #         seat = 0
    #     elif y == self.N:
    #         seat = self.N - 1
    #     else:
    #         seat = (x+y) // 2
    #     # push two intervals by breaking at seat
    #     heapq.heappush(self.pq, (self.dist(x, seat), x, seat))  
    #     heapq.heappush(self.pq, (self.dist(seat, y), seat, y))
    #     return seat
        
    # def leave(self, p):
    #     head = tail = None
    #     for interval in self.pq:  # interval is in the form of (d, x, y)
    #         if interval[1] == p:  
    #             tail = interval
    #         if interval[2] == p:  
    #             head = interval
    #         if head and tail:
    #             break
    #     self.pq.remove(head)
    #     self.pq.remove(tail)
    #     heapq.heapify(self.pq)
    #     heapq.heappush(self.pq, (self.dist(head[1], tail[2]), head[1], tail[2]))



# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)