class Solution:
    def getLucky(self, s: str, k: int) -> int:
        base = ord('a')
        digits = ''
        for i, c in enumerate(s):
            d = ord(c) - base + 1
            digits += str(d)

        total = 0
        for i in range(k):
            total = 0
            for d in digits:
                total = total  + int(d)
            digits = str(total)
            
        return total