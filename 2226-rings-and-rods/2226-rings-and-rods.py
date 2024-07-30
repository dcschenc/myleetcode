class Solution:
    def countPoints(self, rings: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2103.Rings%20and%20Rods
        mask = [0] * 10
        d = {"R": 1, "G": 2, "B": 4}
        for i in range(0, len(rings), 2):
            c = rings[i]
            j = int(rings[i + 1])
            mask[j] |= d[c]
        return mask.count(7)
            
        # hm = defaultdict(set)
        # i, n = 0, len(rings)
        # while i < n - 1:
        #     hm[rings[i + 1]].add(rings[i])
        #     i += 2
        # return len([v for v in hm.values() if len(v) == 3])