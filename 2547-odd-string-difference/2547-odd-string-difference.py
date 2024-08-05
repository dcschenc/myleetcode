class Solution:
    def oddString(self, words: List[str]) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2451.Odd%20String%20Difference
        d = defaultdict(list)
        for s in words:
            t = tuple(ord(b) - ord(a) for a, b in pairwise(s))
            d[t].append(s)
        for ss in d.values():
            if len(ss) == 1:
                return ss[0]

        # hm = defaultdict(list)
        # for w in words:
        #     diff = []
        #     for i in range(1, len(w)):
        #         diff.append(ord(w[i]) - ord(w[i-1]))
        #         hm[tuple(diff)].append(w)
        # for k, v in hm.items():
        #     if len(v) == 1:
        #         return v[0]