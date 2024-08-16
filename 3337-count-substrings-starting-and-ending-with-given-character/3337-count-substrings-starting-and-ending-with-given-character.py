class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        cnt = s.count(c)
        return cnt * (cnt + 1) // 2
        
        n = len(s)
        i = ans = cnt = 0
        while i < n:
            if s[i] == c:
                cnt += 1
                ans += cnt
            i += 1
        return ans