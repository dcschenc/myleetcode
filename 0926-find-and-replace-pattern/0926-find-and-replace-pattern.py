class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return filter(match, words)
        
        ans = []
        n = len(pattern)
        for w in words:
            hm = {}
            hm2 = {}
            i = 0
            while i < n:
                p = pattern[i]
                if p in hm:
                    if hm[p] != w[i]:
                        break
                else:
                    if w[i] in hm2:
                        break
                    hm[p] = w[i]
                    hm2[w[i]] = p
                    
                i += 1               
            if i == n:
                ans.append(w)
        return ans