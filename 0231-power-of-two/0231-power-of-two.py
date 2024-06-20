class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0: return False
        ones = 0
        while n:
            if n & 1 == 1:
                ones += 1
            n >>= 1
        return ones == 1