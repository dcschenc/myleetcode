class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hm = defaultdict(int)
        for v, w in items1 + items2:
            hm[v] += w
        hm = sorted(hm.items())
        return [[v, w] for v, w in hm]