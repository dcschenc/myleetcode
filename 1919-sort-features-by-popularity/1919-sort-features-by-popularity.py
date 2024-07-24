class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1772.Sort%20Features%20by%20Popularity
        cnt = Counter()
        for s in responses:
            for w in set(s.split()):
                cnt[w] += 1
        return sorted(features, key=lambda w: -cnt[w])

        hm = defaultdict(tuple)
        for i, f in enumerate(features):
            hm[f] = (i, 0)
        for r in responses:
            cur = r.split()
            cur = set(cur)
            for w in cur:
                if w in hm:
                    hm[w][1] += 1
            
        feature_pairs = sorted(hm.items(), key = lambda x: (x[1][1], -x[1][0]), reverse=True)
        ans = []
        for k, v in feature_pairs:
            ans.append(k)
        return ans
