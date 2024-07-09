class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hm = {}
        for i, c in enumerate(keyboard):
            hm[c] = i
        pos = 0
        ans = 0
        for c in word:
            ans += abs(hm[c] - pos)
            pos = hm[c]
        return ans
