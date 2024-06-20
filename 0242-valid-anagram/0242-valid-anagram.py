from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = defaultdict(int), defaultdict(int)
        n = len(s)
        for i in range(n):
            count_s[s[i]] += 1      
            count_t[t[i]] += 1
        for i in range(n):
            if count_s[s[i]] != count_t[s[i]]:
                return False
        return True
       
        return sorted(s) == sorted(t)
        return Counter(s) == Counter(t)