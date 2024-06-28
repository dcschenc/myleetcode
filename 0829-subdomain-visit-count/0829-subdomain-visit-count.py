from collections import defaultdict 
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = Counter()
        for s in cpdomains:
            v = int(s[: s.index(' ')])
            for i, c in enumerate(s):
                if c in ' .':
                    cnt[s[i + 1 :]] += v
        return [f'{v} {s}' for s, v in cnt.items()]
        
        hm = defaultdict(int)
        for v in cpdomains:
            c, domain = v.split(' ')
            c = int(c)
            arr = domain.split('.')
            cur = arr[-1]   
            hm[cur] += c
            cur = arr[-2] + '.' + arr[-1]
            hm[cur] += c
            if len(arr) == 3:
                cur = domain
                hm[cur] += c
        return [str(v) + ' ' + k for k, v in hm.items()]