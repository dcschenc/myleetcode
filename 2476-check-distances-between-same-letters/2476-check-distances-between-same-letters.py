class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        hm = {}
        ans = [0] * 25
        base = ord('a')
        for i, c in enumerate(s):
            if c in hm:
                if distance[ord(c) - base] != i - hm[c] - 1:
                    return False
            hm[c] = i
        return True
