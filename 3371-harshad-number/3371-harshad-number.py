class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total = 0
        for d in str(x):
            total = total + int(d)
        return total if x % total == 0 else -1