class Solution:
    def splitNum(self, num: int) -> int:
        num = str(num)
        num = sorted(num)
        a, b = '', ''
        i, n = 0, len(num)
        while i < n:
            a += num[i]
            i += 1
            if i < n:
                b += num[i]
            i += 1
        return int(a) + int(b)