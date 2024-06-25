class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        if m > n:
            a, b = b, a
        if a != b:
            return len(b)
        else:
            return -1
        