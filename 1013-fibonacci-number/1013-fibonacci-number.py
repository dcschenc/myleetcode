class Solution:
    # hm = {}
    @cache
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        # if n in self.hm:
            # return self.hm[n]
        res = self.fib(n-1) + self.fib(n-2)
        # self.hm[n] = res
        return res