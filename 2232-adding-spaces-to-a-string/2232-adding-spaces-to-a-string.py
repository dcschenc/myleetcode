class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n, m = len(s), len(spaces)
        ans = ''
        i, j = 0, 0
        while j < m:
            idx = spaces[j]
            ans += s[i:idx] + ' '
            i = idx
            j += 1
        return ans + s[idx:]
