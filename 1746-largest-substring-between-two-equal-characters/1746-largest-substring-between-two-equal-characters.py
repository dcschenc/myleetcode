class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hm = {}
        ans = -1
        for i, c in enumerate(s):
            if c in hm:
                ans = max(ans, i - hm[c] - 1)
            else:
                hm[c] = i
        return ans