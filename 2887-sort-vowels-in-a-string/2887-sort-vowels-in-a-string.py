class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        vowel = []
        for c in s:
            if c in 'aeiouAEIOU':
                vowel.append(c)
        vowel.sort()
        s, cur = list(s), 0
        for i, c in enumerate(s):
            if c in 'aeiouAEIOU':
                s[i] = vowel[cur]
                cur += 1

        return ''.join(s)