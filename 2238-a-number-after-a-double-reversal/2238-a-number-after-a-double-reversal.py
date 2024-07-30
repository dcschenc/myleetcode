class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0

        num = str(num)
        return num[-1] != '0' or len(num) == 1