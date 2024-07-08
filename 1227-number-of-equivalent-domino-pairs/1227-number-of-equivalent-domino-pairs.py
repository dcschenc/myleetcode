from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1128.Number%20of%20Equivalent%20Domino%20Pairs
        cnt = 0
        hm = defaultdict(int)
        for i, d in enumerate(dominoes):
            # if d[0] > d[1]:
            #     d[1], d[0] = d[0], d[1]
            # key = (d[0], d[1])
            
            key = tuple(sorted(d))
            
            cnt += hm[key]
            hm[key] += 1
        return cnt