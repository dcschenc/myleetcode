from collections import defaultdict
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hm = Counter()
        for w in words:
            for c in w:
                hm[c] += 1
        n = len(words)
        return all(v % n == 0 for v in hm.values())
        # for k, v in hm.items():
        #     if v % len(words) != 0:
        #         return False
        # return True
            