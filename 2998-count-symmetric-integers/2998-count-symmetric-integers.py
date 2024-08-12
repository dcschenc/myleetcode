class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        total = 0
        for num in range(low, high + 1):
            num = str(num)
            n = len(num)
            if n % 2 == 0 and sum(int(d) for d in num[:n//2]) == sum(int(d) for d in num[n//2:]):
                total += 1
        return total