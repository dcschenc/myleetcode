class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total1 = total2 = 0
        for i in range(1, n + 1):
            if i % m != 0:
                total1 += i
            else:
                total2 += i
        return total1 - total2