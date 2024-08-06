class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = -1
        for s in strs:
            if all(c.isdigit() for c in s):
                ans = max(ans, int(s))
            else:
                ans = max(ans, len(s))
        return ans