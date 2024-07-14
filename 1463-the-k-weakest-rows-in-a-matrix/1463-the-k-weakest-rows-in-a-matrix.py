from collections import defaultdict
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hm = defaultdict(int)
        for i in range(len(mat)):
            num_1 = mat[i].count(1)
            hm[i] = num_1
        sorted_items = sorted(hm.items(), key = lambda x: (x[1], x[0]))
        return [ x[0] for x in sorted_items[:k]]