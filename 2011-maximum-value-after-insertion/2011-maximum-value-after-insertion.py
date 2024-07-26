class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x = str(x)
        if n[0] != '-':
            i, m = 0, len(n)
            while i < m:
                if n[i] < x:
                    return n[:i] + x + n[i:]
                i += 1
            return n + x
        else:
            i, m = 0, len(n)
            while i < m:
                if n[i] > x:
                    return n[:i] + x + n[i:]
                i += 1
            return n + x
            