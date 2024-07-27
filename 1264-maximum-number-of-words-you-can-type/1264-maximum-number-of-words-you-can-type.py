class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        broken = set(brokenLetters)
        for w in text.split():
            if not set(w) & broken:
                ans += 1
        return ans