class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for p in paths:
            p = p.split(' ')
            root = p[0]
            for f in p[1:]:
                idx = f.index('(')
                content = f[idx:]
                hm[content].append(root + '/' + f[:idx])
        ans = []
        for k, v in hm.items():
            if len(v) > 1:
                ans.append(v)
        return ans