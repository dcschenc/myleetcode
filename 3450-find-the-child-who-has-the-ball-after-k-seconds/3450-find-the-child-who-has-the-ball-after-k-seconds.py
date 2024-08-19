class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        t, m = divmod(k, n - 1)
        if t % 2 == 1:
            return n - 1 - m
        else:
            return m