class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        i, n = 1, len(word)
        ans = 0
        while i < n:
            if abs(ord(word[i]) - ord(word[i-1])) <= 1:
                ans += 1
                i += 2
            else:
                i += 1
        return ans
