class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(math.sqrt(c))
        while a <= b:
            cur = a**2 + b**2
            if cur == c:
                return True
            elif cur < c:
                a += 1
            else:
                b -= 1
        return False