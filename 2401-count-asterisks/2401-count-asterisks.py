class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        arr = s.split('|')
        for seg in arr[0::2]:
            ans += seg.count('*')
        return ans