from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        ans = ''
        for k in order:
            if k in counter:
                ans += k * counter[k]
                del counter[k]
        for k, v in counter.items():
            ans += k * v
        return ans