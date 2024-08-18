class Solution:
    def compressedString(self, word: str) -> str:
        comp = ''
        i, n = 0, len(word)
        while i < n:
            j = i + 1
            while j < n and word[j] == word[i] and j - i < 9:
                j += 1
            comp += str(j - i) + word[i]
            i = j
        return comp