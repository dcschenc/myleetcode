class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        word = set(word)
        for c in string.ascii_lowercase:
            if c in word and c.upper() in word:
                ans += 1
        return ans