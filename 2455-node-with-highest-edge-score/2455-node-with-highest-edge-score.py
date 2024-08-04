class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        cnt = Counter()
        for i, v in enumerate(edges):
            cnt[v] += i
        ans = 0
        for i in range(len(edges)):
            if cnt[ans] < cnt[i]:
                ans = i
        return ans
        
        hm = defaultdict(int)
        for i in range(len(edges)):
            hm[edges[i]] += i
        res = sorted(hm.items(), key=lambda x: (x[1], -x[0]), reverse=True)
        return res[0][0]
