class Solution:
    def minimumMoves(self, s: str) -> int:
        s = list(s)
        i, ans, n = 0, 0, len(s)
        while i < n:
            if s[i] == 'X':
                ans += 1
                i += 3
            else:
                i += 1
        return ans