from collections import defaultdict
class Solution:
    def partitionString(self, s: str) -> int:
        n = len(s)
        splits = 0
        i = 0
        while i < n:
            hm = {}
            j = i
            while j < n and s[j] not in hm:
                hm[s[j]] = 1
                j += 1
            splits += 1
            i = j
        return splits


        