class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j = 0, 0
        direction = True
        res = ''
        while i < m and j < n:
            if direction:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
            direction = not direction
        if i < m:
            res += word1[i:]
        else:
            res += word2[j:]
        return res