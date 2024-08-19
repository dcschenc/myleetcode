class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        total = 0
        for k, v in counter.items():
            if v % 2 == 1:
                total += 1
            else:
                total += 2
        return total