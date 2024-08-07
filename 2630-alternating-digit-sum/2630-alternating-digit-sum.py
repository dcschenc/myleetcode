class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total = 0
        add = True
        for d in str(n):
            if add:
                total += int(d)
                add = False
            else:
                total -= int(d)
                add = True
        return total