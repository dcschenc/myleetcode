class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        n = len(s)
        i = ans = cnt = 0
        while i < n:
            if s[i] == c:
                cnt += 1
                ans += cnt
            i += 1
        return ans