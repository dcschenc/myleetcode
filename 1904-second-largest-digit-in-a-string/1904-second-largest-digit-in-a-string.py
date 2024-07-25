class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()
        for c in s:
            if c.isdigit():
                digits.add(c)
        if len(digits) < 2:
            return -1
        return int(sorted(list(digits), reverse=True)[1])