class MRUQueue:
    # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1756.Design%20Most%20Recently%20Used%20Queue
    def __init__(self, n: int):
        self.q = list(range(1, n + 1))

    def fetch(self, k: int) -> int:
        ans = self.q[k - 1]
        self.q[k - 1 : k] = []
        self.q.append(ans)
        return ans
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)