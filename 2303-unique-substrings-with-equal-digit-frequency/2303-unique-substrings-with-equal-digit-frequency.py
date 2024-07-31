from collections import Counter, defaultdict
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        # def backtrack(idx, path):
        #     # nonlocal ans         
        #     print(path)   
        #     count = Counter(path)
        #     if len(set(count.values())) == 1:
        #         seen.add(path)
        #     for i in range(idx+1, len(s)):
        #         backtrack(i, path + s[i])        
        n = len(s)
        seen = set()        
        for i in range(n):
            hm = defaultdict(int)
            hm[s[i]] = 1
            seen.add(s[i])
            for j in range(i+1,n):
                hm[s[j]] +=1
                if len(set(hm.values())) == 1:
                    seen.add(s[i:j+1])
        return len(seen)