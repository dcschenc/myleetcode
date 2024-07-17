from collections import defaultdict
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1487.Making%20File%20Names%20Unique
        d = defaultdict(int)
        for i, name in enumerate(names):
            if name in d:
                k = d[name]
                while f'{name}({k})' in d:
                    k += 1
                d[name] = k + 1
                names[i] = f'{name}({k})'
            d[names[i]] = 1
        return names

        hm = defaultdict(int)
        ans = []
        for name in names:
            if name in hm:
                k = hm[name]
                while f'{name}({k+1})'in hm:
                    k += 1
                ans.append(f'{name}({k+1})')
                hm[f'{name}({k+1})'] = 0
                hm[name] = k
            else:
                ans.append(name)
                hm[name] = 0
        return ans

                
