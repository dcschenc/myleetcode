class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter = Counter(s)
        mi = float('inf')
        for k, v in Counter(target).items():
            if k not in counter:
                return 0
            mi = min(mi, counter[k] // v)
        return mi