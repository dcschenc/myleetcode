class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n & 0xaaaaaaaa == 0

        if n == 1: 
            return True
        return int(math.log(n, 4)) ** 4 == n

        if n == 1: 
            return True
        cur = 1
        while cur < n:
            cur *= 4
            if cur == n:
                return True
        return False