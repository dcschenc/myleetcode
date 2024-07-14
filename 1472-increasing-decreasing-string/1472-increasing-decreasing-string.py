from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        hm = Counter(s)
        ans = ''
        incr = True
        while len(hm) > 0:
            if incr:
                for k in sorted(hm.keys()):
                    ans += k
                    hm[k] -= 1
                    if hm[k] == 0:
                        del hm[k]
                incr = False
            else:
                for k in sorted(hm.keys(), reverse=True):
                    ans += k
                    hm[k] -= 1
                    if hm[k] == 0:
                        del hm[k]
                incr = True
        return ans
