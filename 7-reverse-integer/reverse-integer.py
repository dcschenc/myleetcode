class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        minus = 1
        if x < 0:
            x = abs(x)
            minus = -1
        while x > 0:
            res = res * 10 + x%10
            x = x//10
        if res > pow(2,31) - 1:
            res = 0
        return res*minus