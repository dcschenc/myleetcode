from collections import defaultdict 
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0811.Subdomain%20Visit%20Count
        cnt = Counter()
        for s in cpdomains:
            v = int(s[: s.index(' ')])
            for i, c in enumerate(s):
                if c in ' .':
                    cnt[s[i + 1 :]] += v
        return [f'{v} {s}' for s, v in cnt.items()]
        