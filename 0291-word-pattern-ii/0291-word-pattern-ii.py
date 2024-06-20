class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(cp, cs):
            if cp == m and cs == n:
                return True
            if cp == m or cs == n:
                return False
            val = hm.get(pattern[cp], None)
            if val is not None:
                if s[cs:cs + len(val)] == val:
                    ans = backtrack(cp + 1, cs + len(val))
                    if ans: return True
            else:
                for j in range(cs, n):
                    key = s[cs: j + 1]
                    if key not in hm2:
                        hm[pattern[cp]] = key
                        hm2[key] = pattern[cp]
                        ans = backtrack(cp + 1, j + 1)
                        if ans: return True
                        del hm[pattern[cp]]
                        del hm2[key]
            return False
        m, n = len(pattern), len(s)
        hm, hm2 = {}, {}        
        ans = backtrack(0, 0)
        return ans