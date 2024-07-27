class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1943.Describe%20the%20Painting
        diff = defaultdict(int)
        for l, r, v in segments:
            diff[l] += v
            diff[r] -= v
        diff = sorted([pos, v] for pos, v in diff.items())
        for i in range(1, len(diff)):
            diff[i][1] += diff[i-1][1]
        res = []
        # print(diff)
        for i in range(len(diff) - 1):
            if diff[i][1] > 0:
                res.append([diff[i][0], diff[i+1][0], diff[i][1]])
        return res
