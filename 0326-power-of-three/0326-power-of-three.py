class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True
        x = 1
        while x <= n:
            x = x * 3
            if x == n:
                return True
        return False