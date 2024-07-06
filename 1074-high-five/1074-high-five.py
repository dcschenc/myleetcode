from collections import defaultdict
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hm = defaultdict(list)
        for uid, score in items:
            hm[uid].append(score)
        res = {}
        for uid, scores in hm.items():
            scores.sort(reverse=True)
            res[uid] = sum(scores[:5])//5
        sorted_items = sorted(res.items(), key=lambda x: x[0])
        return sorted_items