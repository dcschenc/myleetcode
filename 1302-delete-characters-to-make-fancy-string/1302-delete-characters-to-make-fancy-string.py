class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        ans = s[:2]
        i, n = 2, len(s)
        while i < n:
            if not (s[i] == s[i-1] == s[i-2]):
                ans += s[i]
            i += 1
        return ans
                