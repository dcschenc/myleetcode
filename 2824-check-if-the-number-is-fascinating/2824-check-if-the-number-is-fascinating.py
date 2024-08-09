class Solution:
    def isFascinating(self, n: int) -> bool:
        counter = Counter(str(2 * n) + str(n) + str(3 * n))
        return '0' not in counter and all(counter[k] == 1 for k in '123456789')