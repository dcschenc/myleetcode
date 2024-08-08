class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2606.Find%20the%20Substring%20With%20Maximum%20Cost
        hm = {}
        for c in 'abcdefghijklmnopqrstuvwxyz':
            hm[c] = ord(c) - ord('a') + 1
        for i, c in enumerate(chars):
            hm[c] = vals[i]
        cost = -1
        cur = 0
        for c in s:
            cur = cur + hm[c]
            if cur < 0:
                cur = 0
            cost = max(cost, cur)
        return cost

        # d = {c: v for c, v in zip(chars, vals)}
        # ans = tot = mi = 0
        # for c in s:
        #     v = d.get(c, ord(c) - ord('a') + 1)
        #     tot += v
        #     ans = max(ans, tot - mi)
        #     mi = min(mi, tot)
        # return ans